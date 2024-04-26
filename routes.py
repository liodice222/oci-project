from flask import render_template, request, redirect, url_for, session
from app import app
from models import User
import requests


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET'])
def search():
    username = session.get('username')
    search_query = request.args.get('search')
    response = requests.get(f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{search_query}/JSON')
    compound_info = response.json() if response.status_code == 200 else None
    return {'username': username, 'search_query': search_query, 'compound_info': compound_info}