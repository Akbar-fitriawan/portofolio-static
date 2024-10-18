from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from . import auth_bp
from .forms import LoginForm 
# from .models import User
# from app.extension import db

@auth_bp.route('/auth')
def index():
    return render_template('auth/dashboard.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)
    # if current_user.is_authenticated:
    #     return redirect(url_for('dashboard.index'))
    
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = user.query.filter_by(email=form.email.data).first()
    #     if user and user.check_password(form.password.data):
    #         login_user(user) # login pengguna
    #         flash('Login Berhasil!', 'success')
    #         return redirect(url_for('dashboard.index'))
    #     else:
    #         flash('Email atau password salah.', 'danger')

    # return render_template('auth/login.html'
    #                     #    form=form
    #                        )
    
@auth_bp.route('/logout')
# @login_required
def logout():
    # logout_user()
    flash('Anda telah keluar.', 'success')
    return redirect(url_for('auth.login'))

