# -*- coding: utf8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

APP_NAME = 'myapp'  # your app name

# WTForms
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# DB
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(basedir, 'app.db') +
                               '?check_same_thread=False')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True

DATABASE_QUERY_TIMEOUT = 0.25

# Email server
MAIL_SERVER = ''  # your mailserver
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# Administrator list
ADMINS = ['you@example.com']

# Logging
MEGABYTE = 1024 ** 2
LOG_SIZE_LIMIT = 2 * MEGABYTE
LOG_BACKUP_LIMIT = 10
