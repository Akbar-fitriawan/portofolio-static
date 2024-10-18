from flask import render_template
from . import portfolio_bp
from utils import load_json_data

from datetime import datetime

@portfolio_bp.app_context_processor
def inject_globals():
    return {
        'current_year': datetime.now().year,
        'owner_name': "Akbar Fitriawan",
    }

# routes portfolio lending page
@portfolio_bp.route('/')
@portfolio_bp.route('/home')
def home():

    nav_links = [
        {'name': 'Home', 'url': 'home'},
        {'name': 'About', 'url': 'about'},
        # {'name': 'Services', 'url': 'services'},
        {'name': 'Portfolio', 'url': 'portfolio'},
        {'name': 'Blog', 'url': 'blog'},
        {'name': 'Contact', 'url': 'contact'}
    ]
    
    data = load_json_data('./app/static/data.json')

    return render_template(
        'index.html',
        nav_links=nav_links, 
        personal_details=data['personal_details'], 
        certificates=data['certificates'], 
        educations=data['educations'],
        experiance=data['experiance']
        )

