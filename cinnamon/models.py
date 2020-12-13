from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
 
db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column('id_user', db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String(50), nullable = True, unique = True)
    id_role = db.Column(db.Integer, db.ForeignKey('role.id_role'), nullable = False)
    password = db.Column(db.String(45), nullable = False)
    name = db.Column(db.String(40), nullable = True)
    lastname = db.Column(db.String(45), nullable = True)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    def __repr__(self):
        return '<User %r>' % self.username

class Role(db.Model, RoleMixin):
    id = db.Column('id_role', db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    users = db.relationship('User', lazy = True)
    def __repr__(self):
        return '<Role %r>' % self.name

class Product(db.Model):
    id = db.Column('id_product', db.Integer, primary_key = True)
    product = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)

class Order(db.Model):
    id = db.Column('id_order', db.Integer, primary_key = True)
    date = db.Column(db.DateTime(), nullable = False)
    user_id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable = False)
    status = db.Column(db.Integer, nullable=False)
    cash = db.Column(db.Float, nullable=False)

class OrderProduct(db.Model):
    id = db.Column('id_order_product', db.Integer, primary_key = True)
    product_id_product = db.Column(db.Integer, db.ForeignKey('product.id_product'), nullable = False)
    order_id_order = db.Column(db.Integer, db.ForeignKey('order.id_order'), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)

class Hproduct(db.Model):
    id = db.Column('id_product', db.Integer, primary_key = True)
    product = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(), nullable = False)
