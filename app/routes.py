from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html', name="Home")

@main_bp.route('/about')
def about():
    return render_template('about.html', name="About")

@main_bp.route('/services')
def services():
    return render_template('services.html', name="Services")

@main_bp.route('/whyme')
def why_me():
    return render_template('whyme.html', name="Why me")

@main_bp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', name="Portfolio")

@main_bp.route('/blog')
def blog():
    return render_template('blog.html', name="Blog")

@main_bp.route('/contact')
def contact():
    return render_template('contact.html', name="Contact")

