from flask import Blueprint, render_template

from datetime import datetime

main_bp = Blueprint('main', __name__)

nav_links = [
        {'name': 'Home', 'url': 'main.home'},
        {'name': 'About', 'url': 'main.about'},
        {'name': 'Services', 'url': 'main.services'},
        {'name': 'Why Choose', 'url': 'main.whyme'},
        {'name': 'Portfolio', 'url': 'main.portfolio'},
        {'name': 'Blog', 'url': 'main.blog'},
        {'name': 'Contact', 'url': 'main.contact'}
]

@main_bp.app_context_processor
def inject_globals():
    return {
        'nav_links': nav_links,
        'current_year': datetime.now().year,
        'owner_name': "Akbar Fitriawan"
    }


@main_bp.route('/')
@main_bp.route('/home')
def home():
    
    return render_template(
        'index.html',
        name="Home"
        )

@main_bp.route('/about')
def about():
    
    return render_template('about.html', nav_links=nav_links, name="About")

@main_bp.route('/services')
def services():
    return render_template('services.html', nav_links=nav_links, name="Services")

@main_bp.route('/whyme')
def whyme():
    return render_template('whyme.html', nav_links=nav_links, name="Why choose")

@main_bp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', nav_links=nav_links, name="Portfolio")

@main_bp.route('/blog')
def blog():
    return render_template('blog.html', nav_links=nav_links, name="Blog")

@main_bp.route('/contact')
def contact():
    return render_template('contact.html', nav_links=nav_links, name="Contact")

