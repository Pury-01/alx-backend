#!/usr/bin/env python3
"""Force locale with URL parameter
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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
def get_locale() -> str:
    """
    determine the best match with the supported languages
    """
    # retrieve the locale from the request argument
    locale = request.args.get("locale")
    # check if locale is a valid language
    if locale in app.config["LANGUAGES"]:
        return locale
    # fall back default locale
    return request.accept_languages.best_match(
            app.config["LANGUAGES"]
            )


@app.route('/')
def index():
    """single route
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
