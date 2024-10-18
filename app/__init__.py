from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy



from .extension import init_extensions
from .extension import db, login_manager

from app.auth.models import User

DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SQL_ALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy()
    db.init_app(app)
    
    # Konfigurasi dari config.py
    app.config.from_object('config.Config')

    init_extensions(app)

    # register blueprint
    from .portfolio import portfolio_bp
    from .auth import auth_bp
    # from .blog import blog_bp
    app.register_blueprint(portfolio_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/')
    # app.register_blueprint(auth_bp, url_prefix='/blog')


    # Konfigurasi LoginManager
    login_manager.login_view = 'auth.login'  # URL untuk login
    login_manager.session_protection = 'strong'  # Perlindungan sesi
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    create_db(app)
    
    return app

def create_db(app):
    if not path.exists("app/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")
    else:
        print("Database already exists.")

