#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ index function """
    title = "Welcome to Holberton"
    return render_template(index.html, title=title)


if __name__ == '__main__':
    app.run()
