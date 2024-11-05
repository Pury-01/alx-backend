#!/usr/bin/env python3
"""
flask app with Babel to detect locale from request
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    configures available languages, default locale and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    determine the best match with supported languages.
    """
    return request.accept_languages.best_match(
            app.config['LANGUAGES']
            )


@app.route('/')
def index():
    """single route
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
