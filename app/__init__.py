import os
from flask import Flask, request, current_app, session
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_babel import Babel
# from flask_login import LoginManager
from config import Config

#db = SQLAlchemy()
#migrate = Migrate()
#login = LoginManager()
babel = Babel()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

   # db.init_app(app)
#     migrate.init_app(app, db)
#     login.init_app(app)
#     babel.init_app(app)

    from app.extensions import jinja as jinja_bp
    app.register_blueprint(jinja_bp)

    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    # from app.errors import errors as errors_bp
    # app.register_blueprint(errors_bp)
#     #
#     from app.admin import admin as admin_bp
#     app.register_blueprint(admin_bp, url_prefix='/admin')

#     from app.auth import auth as auth_bp
#     app.register_blueprint(auth_bp, url_prefix='/auth')

    return app


# @babel.localeselector
# def get_locale():
#     return request.accept_languages.best_match(current_app.config['LANGUAGES'])

@babel.localeselector
def get_locale():
    # if the user has set up the language manually it will be stored in the session,
    # so we use the locale from the user settings
    try:
        language = session['language']
    except KeyError:
        language = None
    if language is not None:
        return language
    return request.accept_languages.best_match(Config.LANGUAGES.keys())


# from app import models
