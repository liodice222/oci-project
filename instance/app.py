from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    db = SQLAlchemy(app)

    

#define route back to homepage 
    @app.route('/')
    def home():
        return render_template('home.html')


#define route for search entry
    @app.route('/search', methods=['GET'])
    def search():
        username = session.get('username')
        search_query = request.args.get('search')

    # Here you can add code to search in your database based on the search_query

        return {'username': username, 'search_query': search_query}

    with app.app_context():
        db.create_all()

    return app

app = create_app()

#ensures that db is created and app only run when script is run directly 
if __name__ == '__main__':
    app.run(debug=True)