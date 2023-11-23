import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

oracle_password = os.getenv('DB_PASSWORD')

app.config['SQLALCHEMY_DATABASE_URI'] = f'oracle+cx_oracle://CASTELLANOS_DBP:{oracle_password}@localhost:1521/orcl'

db = SQLAlchemy(app)

from . import routes
