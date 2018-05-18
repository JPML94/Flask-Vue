import os
from flask import Flask
import click
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


from app.api import api_rest, api_bp
from app.client import angler_bp

db = SQLAlchemy()
login = LoginManager()

app = Flask(__name__)
app.register_blueprint(api_bp)
app.register_blueprint(angler_bp)

from . import config
app.logger.info('>>> {}'.format(config.flask_config))

from app import models