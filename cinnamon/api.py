from flask_restful import Resource, Api
from .models import db, User

api = Api()

class HelloWorld(Resource):
    def get(self):
        users = User.query.all()
        print(users)
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')