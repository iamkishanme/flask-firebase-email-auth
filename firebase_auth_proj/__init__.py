from flask import Flask

app = Flask(__name__)

from firebase_auth_proj.auth_app.urls import profile

app.register_blueprint(profile)