from app.extension import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func



# Model user 
class User(db.Model, UserMixin):
    __tablename__ = 'users' # nama tabel

    id = db.Column(db.Integer, primary_key=True) # id pengguna
    username = db.Column(db.String(50), unique=True, nullable=False) # username
    email = db.Column(db.String(50), unique=True, nullable=False)  # email
    password_hash = db.Column(db.String(256), nullable=False) # hash password
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    is_admin = db.Column(db.Boolean, default=False) # apakah pengguna adalah admin


    # Method untuk mangatur password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    # method untuk memeriksa password 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"User {self.username}"