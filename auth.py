#imports
from flask import redirect, render_template, request, session, url_for, Blueprint
from db import db
from models.User import User
#for password hash 
from werkzeug.security import generate_password_hash, check_password_hash

#set up Blueprint
auth = Blueprint('auth', __name__)

#registration route 
@auth.route('/register', methods=['GET', 'POST'])
def register():
    already_user = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        #check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print ("User already exists, please go to Login page")
            already_user = True
            return render_template('register.html', message="User already exists, please go to Login page")
        else:
            already_user = False
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login', message="Registration Successful", already_user = already_user))

    return render_template('register.html', already_user = already_user)

#login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_failed = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            login_failed = True
        else:
            login_failed = False
            session['username'] = user.username
        
        return render_template('home.html', login_failed=login_failed)

    return render_template('home.html', login_failed=login_failed)