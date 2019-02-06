"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.secret_key = '123456'

import Seats.views
