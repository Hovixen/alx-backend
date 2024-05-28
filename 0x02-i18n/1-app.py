#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ config class for babel languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """ index function """
    title = "Welcome to Holberton"
    return render_template("0-index.html", title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
