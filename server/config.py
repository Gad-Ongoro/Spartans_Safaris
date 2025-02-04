import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, make_response, jsonify, session, abort
from flask_mailman import Mail
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import timedelta

from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

# initialize app
app = Flask(__name__)

# app configuration
app = Flask(__name__)
app.secret_key = b'\xb2_8\xcc\xfc\xec3n\xc5\x7f\x01-\xdal[\xc7'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///safaris.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = b'\xb2_8\xcc\xfc\xec3n\xc5\x7f\x01-\xdal[\xc7'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)

app.config["MAIL_SERVER"] = "smtp.fastmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] =  True
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USERNAME"] = "gadongoro1@fastmail.com"
app.config["MAIL_PASSWORD"] = "password"
app.config['MAIL_DEFAULT_SENDER'] = 'gadongoro1@fastmail.com'

mail = Mail(app)

app.json.compact = False

# initialize database
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

bcrypt = Bcrypt(app)
bcrypt.init_app(app)
api = Api(app)

jwt = JWTManager(app)

migrate = Migrate(app, db)
db.init_app(app)
CORS(app)