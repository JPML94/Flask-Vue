""" Client App """

import os
from flask import Blueprint, render_template

angler_bp = Blueprint('client_app', __name__,
                      url_prefix='',
                      static_url_path='',
                      static_folder='./angler/dist',
                      template_folder='./angler/dist',
                      )

@angler_bp.route('/')
def index():
    return render_template('index.html')
