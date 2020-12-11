from flask_restful import Resource, Api, reqparse
from .models import db, User, Role
from flask_security import login_required, current_user, login_user, auth_token_required,SQLAlchemyUserDatastore, Security, utils
from flask import jsonify
from .bl import *

api = Api()

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')

class Auth(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')

        args = parser.parse_args()
        user = user_datastore.get_user(args['username'])
        if user != None:
            if utils.verify_password(args['password'], user.password):
                login_user(user)
                token = user.get_auth_token()
                return {'Authorization-Token' : token}
            else:
                return {'message':'Contraseña incorrecta'}, 401
        else:
            return {'message':'El usuario no existe'}, 401
        return "Sucedió algún error"
    def delete(self):
        utils.logout_user();
        return {'message': 'Log-out exitoso'}, 200

class HelloWorld(Resource):
    def get(self):
        print(current_user)
        if not current_user.is_authenticated:
            return {'message':'Error en la autorización'}, 403
        users = User.query.all()
        print(current_user)
        return {'hello': 'world'}

class SellinList(Resource):
    def get(self):
        print(getSellings())
        return getSellings()

class ProductList(Resource):
    def get(self):
        print(getProducts())
        return getProducts()

class AddProduct(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Chocolate')
        parser.add_argument('10')
        args = parser.parse_args()
        addProduct(args['Chocolate'],args['10'])


api.add_resource(HelloWorld, '/')
api.add_resource(Auth,'/log-in')
api.add_resource(SellinList,'/sellings')
api.add_resource(ProductList, '/list-product')
api.add_resource(AddProduct, '/add-product')
