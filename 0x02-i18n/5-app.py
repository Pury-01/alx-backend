#!/usr/bin/env python3
"""Force locale with URL parameter
"""
from flask import Flask, render_template, request, g
from typing import Optional
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    """single route to the template
    """
    return render_template('5-index.html')


def get_user() -> Optional[dict]:
    """
    retrieves a user dictionary if login_as parameter is valid
    """
    user_id = request.args.get("login_as")
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """
    set the logged-in user to flask.g.user if available.
    """
    g.user = get_user()


if __name__ == '__main__':
    app.run(debug=True)
