# app.py
## Final Project Back-end belongs here

# Running Flask in Testing
# > flask --debug run

import pandas as pd
import pickle
import os

from collections import Counter
from config import UPLOAD_FOLDER, MAX_FILE_SIZE_IN_MEGABYTES, SECRET_KEY
from features import extract_features
from flask import Flask, request, render_template, abort, redirect, url_for
from werkzeug.utils import secure_filename
from utils.file_handling import file_is_allowed, convert_mp3_to_wav, split_audio_chunks

# Initialize Flask App
app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE_IN_MEGABYTES * 1000 * 1000
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if filename != '':
        if not file_is_allowed(filename):
            abort(400)
        uploaded_file.save(file)
    return redirect(url_for('.preprocess', file=file))


@app.route('/preprocess', methods=['GET', 'POST'])
def preprocess():
    file = request.args.get('file', None)
    if file is None:
        abort('404')
    if os.path.splitext(file)[1] == '.mp3':
        file = convert_mp3_to_wav(file)
        return redirect(url_for('.classify', file=file))
    return redirect(url_for('.classify', file=file))


@app.route('/classify', methods=['GET', 'POST'])
def classify():
    file = request.args.get('file', None)
    if file is None:
        abort('404')
    
    audio_chunks = split_audio_chunks(file)
    predictions = []
    for chunks in audio_chunks:
        feature = extract_features(chunks)
        feature = pd.DataFrame(feature, index=[0])
        predictions.append(model.predict(feature)[0])
    predictions = [f"{i[0]} ({round(i[1] / len(predictions) * 100)}%)" for i in Counter(predictions).most_common(3)]
    result = ", ".join(predictions)
    return render_template('index.html', result=str(result))
    

if __name__ == '__main__':
    app.run(debug=True)