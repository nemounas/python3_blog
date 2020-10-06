class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@localhost/test1'
    SECRET_KEY = 'some secret very very'

    # flask_security

    SECURITY_PASSWORD_SALT = 'Salt'
    SECURITY_PASSWORD_HASH = 'sha256_crypt'
