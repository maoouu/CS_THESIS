# app.py
## Final Project Back-end belongs here

# Running Flask in Testing
# > flask --debug run

from flask import Flask, render_template

# Initialize Flask App
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')