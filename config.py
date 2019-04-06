import os
import pymysql

basedir = os.path.abspath(os.path.dirname(__file__))
pymysql.install_as_MySQLdb()


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/nn_assignment'
    UPLOAD_FOLDER = '/TrainingImages'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/nn_assignment'
    UPLOAD_FOLDER = '/TrainingImages'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('APP_TESTING_DATABASE_URI')
    UPLOAD_FOLDER = '/TrainingImages'


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': ProductionConfig,
}
