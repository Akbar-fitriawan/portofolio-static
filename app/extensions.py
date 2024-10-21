from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin

# Inisialisasi ekstensi Flask

# CSRF protection
csrf = CSRFProtect()

# Database ORM (SQLAlchemy)
db = SQLAlchemy()
# Migrasi database
migrate = Migrate()
# Pengiriman email
mail = Mail()
# Autentikasi pengguna
login_manager = LoginManager()

# Password hashing
bcrypt = Bcrypt()

# Admin dashboard (opsional)
admin = Admin(template_mode='bootstrap4')

# Fungsi untuk menginisialisasi semua ekstensi
def init_extensions(app):
    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    admin.init_app(app)
