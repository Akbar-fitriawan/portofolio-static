from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from .extensions import init_extensions, db, login_manager
from app.auth.models import User

DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    
    # Konfigurasi database
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    # Mengatur konfigurasi dari config.py
    app.config.from_object('config.Config')

    # Inisialisasi ekstensi
    init_extensions(app)

    # Mendaftarkan blueprint
    from .portfolio import portfolio_bp
    from .auth import auth
    # from .blog import blog_bp
    app.register_blueprint(portfolio_bp, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    # app.register_blueprint(auth_bp, url_prefix='/blog')

    # Konfigurasi LoginManager
    login_manager.login_view = 'auth.login'  # URL untuk login
    # login_manager.session_protection = 'strong'  # Perlindungan sesi
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Panggil fungsi untuk membuat database
    create_db(app)
    
    return app

def create_db(app):
    if not path.exists("app/" + DB_NAME):
        with app.app_context():  # Pastikan kita berada di dalam konteks aplikasi
            db.create_all()  # Panggil create_all tanpa argumen app
        print("Created Database!")
    else:
        print("Database alraedy exsist..")


