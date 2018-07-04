"""Making directory a package"""
from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

from app.auth.authenticate import auth_blueprint
app.register_blueprint(auth_blueprint)
from app.views import ride_blueprint
app.register_blueprint(ride_blueprint)
