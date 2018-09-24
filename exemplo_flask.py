#!/usr/bin/python3
from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    return datetime.now().strftime('%d-%m-%y  %H:%M:%S')

@app.route('/login')
def login():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)