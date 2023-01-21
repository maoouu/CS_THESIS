# app.py
## Final Project Back-end belongs here

# Running Flask in Testing
# > flask --debug run

import pickle

from config import UPLOAD_FOLDER, MAX_FILE_SIZE_MEGABYTES, SECRET_KEY
from flask import Flask, render_template

# Initialize Flask App
app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE_MEGABYTES
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    pass


@app.route('/classify', methods=['POST'])
def classify():
    pass


if __name__ == '__main__':
    app.run(debug=True)