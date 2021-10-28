import os
from os import environ
# import redis

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = '3qHnMDgasH9zqfc8L2yyomwbABpUyxvH6VESu5uo9kAkmmHRnQEjn3BKArsPGDgzrMHKuLZC9yPEZJ6'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir, 'app.sqlite')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/orione'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    FLASK_ENV = environ.get('FLASK_ENV')

    # LANGUAGES = ['en', 'es']

    LANGUAGES = {
        'en': 'English',
        'es': 'Spanish'
    }

    # Flask-Session
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = redis.from_url('redis://localhost:6379')

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # Admin account
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'password')
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
    ADMIN_EMAIL = os.environ.get(
        'ADMIN_EMAIL', 'admin@admin.com')
    # LANGUAGES = ['en', 'es']
    # MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    # POSTS_PER_PAGE = 25

    # File Upload

    FILE_FOLDER = os.path.join(basedir, 'files/')



