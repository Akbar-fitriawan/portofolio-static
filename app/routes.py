from flask import Blueprint, render_template

from datetime import datetime

main_bp = Blueprint('main', __name__)


@main_bp.app_context_processor
def inject_globals():
    return {
        'current_year': datetime.now().year,
        'owner_name': "Akbar Fitriawan"
    }


@main_bp.route('/')
@main_bp.route('/home')
def home():

    nav_links = [
        {'name': 'home', 'url': 'home'},
        {'name': 'About', 'url': 'about'},
        {'name': 'Services', 'url': 'services'},
        {'name': 'Portfolio', 'url': 'portfolio'},
        {'name': 'Contact', 'url': 'contact'}
    ]
    
    return render_template(
        'index.html',
        nav_links=nav_links
        )

# @main_bp.route('/about')
# def about():
    
#     return render_template('about.html', name="About")

# @main_bp.route('/services')
# def services():
#     return render_template('services.html', name="Services")


# @main_bp.route('/portfolio')
# def portfolio():
#     return render_template('portfolio.html', name="Portfolio")

# @main_bp.route('/blog')
# def blog():
#     return render_template('blog.html', name="Blog")

# @main_bp.route('/contact')
# def contact():
#     return render_template('contact.html', name="Contact")

