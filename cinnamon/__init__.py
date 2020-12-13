import os

from flask import Flask
from .models import db, User, Role
from .api import api, user_datastore
from flask_security import SQLAlchemyUserDatastore, Security
from flask_cors import CORS, cross_origin


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS()
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECURITY_USER_IDENTITY_ATTRIBUTES'] = 'username'
    app.config['SECRET_KEY'] = 'huachimingosal100'
    app.config['SECURITY_PASSWORD_SALT'] = 'huachimingosal100'
    app.config['DEBUG'] = True
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 250
    #app.config['SESSION_COOKIE_HTTPONLY']= False

    @app.after_request
    def creds(response):
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    # Initialize flask modules (Rest and SQLAlchemy)
    db.init_app(app)
    api.init_app(app)
    cors.init_app(app, supports_credentials=True,
                  origins='http://localhost:8080')

    security = Security(app, user_datastore)

    return app
