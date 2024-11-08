#!/usr/bin/env python3
"""Display current time based on locale and timezone settings"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from datetime import datetime
import pytz


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration for Flask app with supported languages and defaults"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """Get user from login_as parameter if available"""
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Set the user as a global if found"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine the best match with the supported languages"""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> str:
    """Determine the appropriate timezone for the user"""
    tz_param = request.args.get("timezone")
    if tz_param:
        try:
            return pytz.timezone(tz_param)
        except pytz.UnknownTimeZoneError:
            pass
    if g.user and g.user.get("timezone"):
        try:
            return pytz.timezone(g.user["timezone"])
        except pytz.UnknownTimeZoneError:
            pass
    return pytz.timezone(app.config["BABEL_DEFAULT_TIMEZONE"])


@app.route('/')
def index():
    """
    Route to the homepage displaying the current time
    based on user's locale and timezone
    """
    current_time = datetime.now(get_timezone()).strftime('%c')
    return render_template(
            'index.html',
            current_time=current_time
            )


if __name__ == "__main__":
    app.run(debug=True)
