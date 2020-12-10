import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'do-or-do-not-there-is-no-try'
    AUTOCRUD_METADATA_ENABLED = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:987654321@localhost/library?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False