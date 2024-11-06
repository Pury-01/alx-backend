#!/usr/bin/env python3
"""
Force locale with URL parameter and user login mock,
with user locale preferences.
"""
from flask import Flask, render_template, request, session, g
from flask_babel import Babel, _
from typing import Optional


app = Flask(__name__)
babel = Babel(app)


# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Configures available languages, default locale, timezone, and session key.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    SECRET_KEY = "your_secret_key_here"


app.config.from_object(Config)


def get_user() -> Optional[dict]:
    """
    Retrieves a user dictionary if login_as parameter is valid, else None.
    """
    user_id = request.args.get("login_as")
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Set the logged-in user to flask.g.user if available.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages.
    Prioritize locale from URL, then user settings, then headers.
    """
    # Locale from URL parameter
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    # Locale from user settings if the user is logged in
    if g.user and g.user.get("locale") in\
            app.config["LANGUAGES"]:
        return g.user["locale"]

    # Locale from request header
    return request.accept_languages.best_match(
            app.config["LANGUAGES"]
            )


@app.route('/')
def index() -> str:
    """Render the main template."""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
