import os
from dotenv import load_dotenv

load_dotenv('.env')

class Config:
    # app secret key
    SECRET_KEY = os.getenv('SECRET_KEY')
    # # Mail konfigurasi
    # MAIL_SERVER = os.getenv('MAIL_SERVER')
    # MAIL_PORT = int(os.getenv('MAIL_PORT'))
    # MAIL_USE_TLS = os.getenv('MAIL_USE_TLS').lower() in ['true', '1', 't']
    # MAIL_USE_SSL = os.getenv('MAIL_USE_SSL').lower() in ['true', '1', 't']
    # MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    # # MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    
    # # EmailJS configuration
    # EMAILJS_SERVICE_ID = os.getenv('EMAILJS_SERVICE_ID')
    # EMAILJS_TEMPLATE_ID = os.getenv('EMAILJS_TEMPLATE_ID')
    # EMAILJS_USER_ID = os.getenv('EMAILJS_USER_ID')