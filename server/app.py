#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db

# create a Flask obj
app = Flask(__name__)

# 1. configure the db in app itself using 'config' attr: connect db
# set up a db file path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# 4. heed the warning by setting SQLALCHEMY_TRACK_MODIFICATIONS to False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 2. import Migrate class to set up migrations 
# passing FLask app instance and SQLAlchemy instance as params
migrate = Migrate(app, db)

# 3. initialise app / Flask-Migrate for use within db configuration
db.init_app(app)



if __name__ == "__main__":
    app.run(port=5555, debug=True)