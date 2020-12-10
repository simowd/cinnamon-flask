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