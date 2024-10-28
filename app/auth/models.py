from app.extensions import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# Model user 
class User(db.Model, UserMixin):
    __tablename__ = 'users' # nama tabel

    id = db.Column(db.Integer, primary_key=True) # id pengguna
    name = db.Column(db.String(50), unique=True, nullable=False) # username
    email = db.Column(db.String(50), unique=True, nullable=False)  # email
    password = db.Column(db.String(256), nullable=False) # hash password
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
   
