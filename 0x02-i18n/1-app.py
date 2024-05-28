#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LANG'] = 'en'
app.config['BABEL_SUPPORTED_LANG'] = ['en', 'fr']

babel = Babel(app)


@app.route('/')
def index():
    """ index function """
    title = "Welcome to Holberton"
    return render_template("0-index.html", title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
