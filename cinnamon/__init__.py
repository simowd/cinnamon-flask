import os

from flask import Flask
from .models import db, User, Role
from .api import api, user_datastore
from flask_security import SQLAlchemyUserDatastore, Security


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zylzojixmwbqsg:1ade1d6715be01d74e0ea91cced1778324ad5bef35016a1103d5adb01073c561@ec2-34-237-166-54.compute-1.amazonaws.com:5432/db8od3ulqain3f'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECURITY_USER_IDENTITY_ATTRIBUTES'] = 'username'    
    app.config['SECRET_KEY'] = 'huachimingosal100'
    app.config['SECURITY_PASSWORD_SALT'] = 'huachimingosal100'
    app.config['DEBUG'] = True
    

    #Initialize flask modules (Rest and SQLAlchemy)
    db.init_app(app)
    api.init_app(app)

    security = Security(app, user_datastore)
    
    

    return app