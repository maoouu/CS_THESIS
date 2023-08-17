# app.py

import pandas as pd
import pickle
import os

from collections import Counter
from config import UPLOAD_FOLDER, MAX_FILE_SIZE_IN_MEGABYTES, SECRET_KEY
from features import extract_features
from flask import Flask, request, render_template, abort, redirect, url_for
from werkzeug.utils import secure_filename
from utils.file_handling import file_is_allowed, convert_mp3_to_wav, split_audio_chunks
from utils.youtube_converter import download_youtube_audio, get_title

# Initialize Flask App
app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE_IN_MEGABYTES * 1000 * 1000
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        input_file = request.form.get('input')

        if input_file and input_file.startswith("https://www.youtube.com/"):
            # Download and convert YouTube audio to WAV
            audio_file = download_youtube_audio(input_file)
            wav_file = convert_mp3_to_wav(audio_file)
            return redirect(url_for('.classify', file=wav_file, filename='Unknown'))

        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        file = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        if filename != '':
            if not file_is_allowed(filename):
                abort(400)
            uploaded_file.save(file)
            wav_file = convert_mp3_to_wav(file)
            return redirect(url_for('.classify', file=wav_file, filename=filename[:-4]))

    return render_template('index.html')  # Render the upload form if it's a GET request



@app.route('/preprocess', methods=['GET', 'POST'])
def preprocess():
    file = request.args.get('file', None)
    filename = request.args.get('filename', 'N/A')
    if file is None:
        abort('404')
    if os.path.splitext(file)[1] == '.mp3':
        file = convert_mp3_to_wav(file)
        return redirect(url_for('.classify', file=file, filename=filename))
    return redirect(url_for('.classify', file=file, filename=filename))


@app.route('/classify', methods=['GET', 'POST'])
def classify():
    file = request.args.get('file', None)
    filename = request.args.get('filename', 'N/A')
    if file is None:
        abort('404')
    
    audio_chunks = split_audio_chunks(file)
    predictions = []
    for chunks in audio_chunks:
        feature = extract_features(chunks)
        feature = pd.DataFrame(feature, index=[0])
        predictions.append(model.predict(feature)[0])
    result = Counter(predictions).most_common(1)[0][0]
    return render_template('index.html', result=str(result), filename=str(filename))

if __name__ == '__main__':
    app.run(debug=True)