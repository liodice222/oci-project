from flask import render_template, request, redirect, url_for, session
from app import app
from models import User

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET'])
def search():
    username = session.get('username')
    search_query = request.args.get('search')
    return {'username': username, 'search_query': search_query}