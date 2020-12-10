from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(45), nullable = False)
    name = db.Column(db.String(40), nullable = True)
    lastname = db.Column(db.String(45), nullable = True)
    def __repr__(self):
        return '<User %r>' % self.username