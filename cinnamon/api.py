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
                return {'Authorization-Token' : token , 'id_user': user.id}
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
        if not current_user.is_authenticated:
            return {'message': 'Error en la autenticación'}, 403
        parser = reqparse.RequestParser()
        parser.add_argument('Authentication-Token')
        parser.add_argument('id_user')
        args = parser.parse_args()
        print(args)
        #status = auth_check(args['Authentication-Token'], args['id_user'])
        users = User.query.all()
        #print(status)
        return {'hello': 'world'}


class OrdersBD(Resource):
    def get(self):
        if not current_user.is_authenticated:
            return {'message': 'Error en la autenticación'}, 403
        parser = reqparse.RequestParser()
        parser.add_argument('today')
        parser.add_argument('tomorrow')
        args = parser.parse_args()
        return getSellingsByDate(args['today'], args['tomorrow'])
        

class Orders(Resource):
    def get(self):
        if not current_user.is_authenticated:
            return {'message': 'Error en la autenticación'}, 403
        print(getSellings())
        return getSellings()

    def post(self):
        if not current_user.is_authenticated:
            return {'message': 'Error en la autenticación'}, 403
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        parser.add_argument('cash')
        parser.add_argument('ord',action="append")
        args = parser.parse_args()
        addOrder(args['id'], args['cash'], args['ord'])
        
        return {'message': 'Request Successful!'}, 200

    def delete(self):
        if not current_user.is_authenticated:
            return {'message': 'Error en la autenticación'}, 403
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        deleteOrder(args['id'])
        return {'message': 'Request Successful!'}, 200

class Product(Resource):
    def get(self):
        if not current_user.is_authenticated:
            return {'message': 'Error en la autenticación'}, 403
        print(getProducts())
        return getProducts()

    def post(self):
        if not current_user.is_authenticated:
            return {'message': 'Error en la autenticación'}, 403
        parser = reqparse.RequestParser()
        parser.add_argument('product')
        parser.add_argument('price')
        args = parser.parse_args()
        addProduct(args['product'],args['price'])
        return {'message': 'Request Successful!'}, 200

    def put(self):
        if not current_user.is_authenticated:
            return {'message': 'Error en la autenticación'}, 403
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        parser.add_argument('product')
        parser.add_argument('price')
        args = parser.parse_args()
        modifyProduct(args['id'], args['product'], args['price'])
        return {'message': 'Request Successful!'}, 200

    def delete(self):
        if not current_user.is_authenticated:
            return {'message': 'Error en la autenticación'}, 403
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args=parser.parse_args()
        deleteProduct(args['id'])
        return {'message': 'Request Successful!'}, 200

api.add_resource(HelloWorld, '/')
api.add_resource(Auth,'/log-in')
api.add_resource(Orders,'/order')
api.add_resource(OrdersBD,'/order/by-date')
api.add_resource(Product, '/product')


def auth_check(auth_token, id_user):
    user = user_datastore.get_user(id_user)
    tokenstat = (utils.get_token_status(auth_token, 'confirm', 'LOGIN'))
    print(tokenstat)
    if auth_token == user.get_auth_token():
        return True
    else:
        return False