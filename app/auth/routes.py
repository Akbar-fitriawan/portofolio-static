from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from .models import User
from app.extensions import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index_posts'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        # Validasi input email dan password
        if not email or not password:
            flash("Please enter both email and password.", "warning")
            return redirect(url_for('auth.login'))

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details and try again.", "danger")
            return redirect(url_for('auth.login'))

        login_user(user, remember=remember)
        return redirect(url_for('auth.index_posts'))

    # nav_links = [{'name': 'Back to Home', 'url': url_for('/home')}]
    return render_template('auth/login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index_post'))

    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        # Validasi input
        if not email or not name or not password:
            flash("Please fill out all fields.", "warning")
            return redirect(url_for('auth.signup'))

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email address already exists', "warning")
            return redirect(url_for('auth.signup'))

        new_user = User(
            email=email, 
            name=name,
            password=generate_password_hash(password, method='pbkdf2:sha256')
        )

        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('auth.login'))

    # nav_links = [{'name': 'Back to Home', 'url': url_for('home')}]
    return render_template('auth/signup.html')


@auth.route('/index_posts')
@login_required
def index_posts():
    nav_links = [
        {'name': 'New Post','url': url_for('auth.create_post')},
        # {'name': 'Posts', 'url': url_for('auth.index_posts')},
        {'name': 'Statistics', 'url': url_for('auth.statistics')},
        {'name': 'Comment', 'url': url_for('auth.comment')},
        {'name': 'Logout', 'url': url_for('auth.logout')}
    ]
    return render_template('auth/dashboard.html', nav_links=nav_links, name=current_user.name)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))


# Placeholder routes for other functionalities (modify according to your needs)
@auth.route('/create_post')
@login_required
def create_post():
    return render_template('auth/create_post.html')


@auth.route('/statistics')
@login_required
def statistics():
    return "This is where you can view blog statistics."


@auth.route('/comment')
@login_required
def comment():
    return "This is where you can manage comments."
