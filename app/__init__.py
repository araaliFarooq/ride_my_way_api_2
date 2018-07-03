"""Making directory a package"""
from flask import Flask

app = Flask(__name__)

# from app import views
from app.auth.Authenticate import auth_blueprint
app.register_blueprint(auth_blueprint)

