import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecret'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class BasicConfig(Config):
    DEBUG=True
    USERNAME = os.environ.get('DB_USERNAME') or 'root'
    PASSWORD = os.environ.get('DB_PASSWORD') or ''
    SERVER = os.environ.get('SERVER') or 'localhost'
    DB_NAME = os.environ.get('DB_NAME') or 'blog_db'
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{ USERNAME }:{ PASSWORD }@{ SERVER }/{ DB_NAME }'

config ={
    'default': BasicConfig
}
