from flask import Flask
from db import db
from dotenv import load_dotenv
import os
from auth import auth as auth_blueprint


load_dotenv()

app = Flask(__name__)
app.register_blueprint(auth_blueprint)


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


db.init_app(app)


