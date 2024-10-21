from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from . import auth
from .forms import LoginForm 
from .models import User
from app.extensions import db
from werkzeug.security import check_password_hash

@auth.route('/dashboard')
def index():
    return render_template('auth/dashboard.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():

    nav_links = [
        {'name': 'Back to Home', 'url': 'home'}
    ]
    
    form = LoginForm()
    if form.validate_on_submit():
        # Perbaiki ini dari user.query ke User.query
        user = User.query.filter_by(email=form.email.data).first()
        print("user found {user}")

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)  # login pengguna
            flash('Login Berhasil!', category='success')
            return redirect(url_for('auth.index'))
        else:
            flash('Email atau password salah.',  category='danger')

    return render_template('auth/login.html', form=form, nav_links=nav_links)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Anda telah keluar.', 'success')
    return redirect(url_for('auth.login'))
