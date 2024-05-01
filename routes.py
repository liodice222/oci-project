from flask import render_template, request, redirect, url_for, session
from app import app
from db import db
from models import User
import requests




@app.route('/')
def home():
    print("rendering home.html")
    return render_template('home.html')



@app.route('/search', methods=['GET'])
def search():
    username = session.get('username')
    search_query = request.args.get('search')
    #added print statements for debugging
    print(f'Search Query: {search_query}')  
    
    try:
        response = requests.get(f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{search_query}/JSON')
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        response = None

    compound_info = response.json() if response and response.status_code == 200 else None
    compound_data = {}

    if compound_info:
        compound = compound_info['PC_Compounds'][0]
        props = compound['props']

        # Extracting the IUPAC name, charge, and molecular weight
        for prop in props:
            if 'name' in prop['urn'] and 'label' in prop['urn']:
                if prop['urn']['name'] == 'Allowed' and prop['urn']['label'] == 'IUPAC Name':
                    compound_data['iupac_name'] = prop['value']['sval']
                elif prop['urn']['label'] == 'Molecular Weight':
                    compound_data['molecular_weight'] = prop['value']['sval']

        compound_data['charge'] = compound['charge']

        

        # # Generate the molecule image
        # molecule = Chem.MolFromSmiles(search_query)
        # Draw.MolToFile(molecule, f'static/{search_query}.png')

        

    print(f'API Response: {compound_data}')

    return {'username': username, 'search_query': search_query, 'compound_info': compound_data}

