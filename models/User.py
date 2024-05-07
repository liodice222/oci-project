from flask_login import UserMixin
from db import db

#set up user model to be stored in user database  
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

#search model to be stored in analytics database 
class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    search_query = db.Column(db.String(200))
    search_result = db.Column(db.Text)

    #define relationship with user model
    user = db.relationship('User')