from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
from server.config import DEBUG_MODE, SECRET_KEY,  SQLALCHEMY_TRACK_MODIFICATIONS, SQLALCHEMY_DATABASE_URI, \
    JWT_BLACKLIST_ENABLED, JWT_BLACKLIST_TOKEN_CHECKS, JWT_ACCESS_TOKEN_EXPIRES


app = Flask(__name__)

app.config['DEBUG'] = DEBUG_MODE
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['JWT_SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)

app.config['JWT_BLACKLIST_ENABLED'] = JWT_BLACKLIST_ENABLED
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = JWT_BLACKLIST_TOKEN_CHECKS
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES


from server.controllers import *
