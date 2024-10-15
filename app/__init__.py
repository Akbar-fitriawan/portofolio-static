from flask import Flask
from flask_mail import Mail
# from flask_wtf.csrf import CSRFProtect  # Tambahkan import CSRF


mail = Mail()
# csrf = CSRFProtect()  # Inisialisasi CSRF protection

def create_app():
    app = Flask(__name__)
    
        # Konfigurasi dari config.py
    app.config.from_object('config.Config')

    # Inisialisasi mail dan csrf
    mail.init_app(app)
    # csrf.init_app(app)
    
    # Import blueprints (untuk modularisasi jika dibutuhkan)
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
