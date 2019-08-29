import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
import marshmallow_sqlalchemy

# Get the Flask app instance
app = Flask(__name__)
api = Api(app)


# Build the Sqlite ULR for SqlAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
sqlite_url = "sqlite:///" + os.path.join(basedir, "test.db")

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
#ma = Marshmallow(app)
ma = marshmallow_sqlalchemy