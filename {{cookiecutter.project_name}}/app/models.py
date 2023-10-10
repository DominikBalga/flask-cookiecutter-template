from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_requred, current_user, logout_

#initialized database
db = SQLAlchemy()

# Model: User - columns: id (int, primary_key), email (string, unique), password (string) 
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))