# File: main.py
# About: A Simple Flask App
# Author: Matthew Kearns
# Email: mattdkearns@gmail.com

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    """index.html"""
    return open('./index.html', 'r').read()

@app.route('/about.html')
def about():
    """about.html"""
    return open('./about.html', 'r').read()


if __name__ == '__main__':
    app.run()

