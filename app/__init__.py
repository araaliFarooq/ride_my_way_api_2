"""Making directory a package"""
from flask import Flask

app = Flask(__name__)

from app.auth.authenticate import auth_blueprint
app.register_blueprint(auth_blueprint)
from app.views import ride_blueprint
app.register_blueprint(ride_blueprint)

app.config['JWT_SECRET_KEY'] = 'sec-def-oscar-zulu-3-zero-niner'
from flask_jwt_extended import JWTManager
jwt = JWTManager(app)
