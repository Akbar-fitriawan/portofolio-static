from flask import Blueprint, render_template
from utils import load_json_data

from datetime import datetime

main_bp = Blueprint('main', __name__)


@main_bp.app_context_processor
def inject_globals():
    return {
        'current_year': datetime.now().year,
        'owner_name': "Akbar Fitriawan",

    }


@main_bp.route('/')
@main_bp.route('/home')
def home():

    nav_links = [
        {'name': 'Home', 'url': 'home'},
        {'name': 'About', 'url': 'about'},
        {'name': 'Services', 'url': 'services'},
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
        educations=data['educations'])


