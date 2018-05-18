from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwcrypto
from app import db, login


class User(UserMixin, db.Model):
    ___tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    last_login = db.Column(db.String(120), default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
        
    def get_reset_password_token(self, expires_in=600):
        return jwcrypto.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')
    
    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwcrypto.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class JobPost(db.Model):
    ___tablename__ = 'job_posts'
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(120))
    location = db.Column(db.String(120))
    salary = db.Column(db.Integer)
    url = db.Column(db.String(240))

    def __repr__(self):
        return '<JobPost {}>'.format(self.job_title)


class Company(db.Model):
    ___tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    location = db.Column(db.String(128))
    description = db.Column(db.String(240))
    website = db.Column(db.String(64))