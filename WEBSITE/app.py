# app.py
## Final Project Back-end belongs here

# Running Flask in Testing
# > flask --debug run

import pickle

from flask import Flask, render_template

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = ['wav', 'mp3']

# Check if filename is wav or mp3
def is_allowed_file_extension(filename, ALLOWED_EXTENSIONS):
    file_extension = filename.split('.')[-1].lower()
    return file_extension in ALLOWED_EXTENSIONS


# Initialize Flask App
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    pass


@app.route('/classify', methods=['POST'])
def classify():
    pass