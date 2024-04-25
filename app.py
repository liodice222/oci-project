from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

#set up user model to be stored in user database  
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

#define route back to homepage 
@app.route('/')
def home():
    return render_template('home.html')

#ensures that db is created and app only run when script is run directly 
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    

@app.route('/search', methods=['GET'])
def search():
    username = session.get('username')
    search_query = request.args.get('search')

    # Here you can add code to search in your database based on the search_query

    return {'username': username, 'search_query': search_query}