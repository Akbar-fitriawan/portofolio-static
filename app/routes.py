from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_mail import Message

from config import Config
from . import mail
from datetime import datetime
from utils import load_json_data

# mail = Mail()

main_bp = Blueprint('main', __name__)

@main_bp.app_context_processor
def inject_globals():
    return {
        'current_year': datetime.now().year,
        'owner_name': "Akbar Fitriawan",
    }


@main_bp.route('/', methods=['GET', 'POST'])
@main_bp.route('/send-message')
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


    return render_template('index.html', 
                           nav_links=nav_links, 
                           personal_details=data['personal_details'], 
                           certificates=data['certificates'], 
                           educations=data['educations'],
                           experiance=data['experiance'])



# # Route untuk form
# @main_bp.route('/send-message', methods=['POST'])
# def send_message():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         subject = request.form['subject']
#         message = request.form['message']

#     if not name or not email or not subject or not message:
#            flash('Semua kolom harus diisi!', 'danger')
#            return redirect(url_for('main.home'))

#     # Membuat pesan email
#     msg = Message(
#                 subject=f"Message from {name}: {subject}",
#                 sender=email,
#                 recipients=['akbarfitriawan12@gmail.com'] # Email tujuan (Gmail kamu)
#                 reply_to=['a']
#             )
    
#     msg.body = f"From: {name} <{email}>\n\n{message}"

#     # Mengirim email
#     try:
#         mail.send(msg)
#         flash('Message sent successfully!', 'success')
#     except Exception as e:
#         flash(f'Failed to send message. Error: {e}', 'danger')

#     return redirect(url_for('main.home'))