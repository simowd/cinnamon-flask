import os

from flask import Flask
from .models import db
from .api import api

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zylzojixmwbqsg:1ade1d6715be01d74e0ea91cced1778324ad5bef35016a1103d5adb01073c561@ec2-34-237-166-54.compute-1.amazonaws.com:5432/db8od3ulqain3f'
    db.init_app(app)
    api.init_app(app)

    return app