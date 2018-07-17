# File: main.py
# About: A Simple Flask App
# Author: Matthew Kearns
# Email: mattdkearns@gmail.com

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Index.html"""
    #return 'Hello, world!'
    return open('./index.html', 'r').read()

if __name__ == '__main__':
    app.run()

