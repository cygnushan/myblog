#!/usr/bin/env python
# coding: utf-8

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    ARTICLES_PER_PAGE = 10
    COMMENTS_PER_PAGE = 6
    SECRET_KEY = os.environ.get('SECRET_KEY') or '!qaz@wsx'
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY') or '@wsx#edc'  # for csrf protection, default SECRET_KEY

    # MAIL SETTING
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465  # 465 or 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = '[Cygnushan Blog]'
    MAIL_SENDER = 'Cygnus Han<cygnushan@foxmail.com>'

    @staticmethod
    def init_app(app):
        pass
