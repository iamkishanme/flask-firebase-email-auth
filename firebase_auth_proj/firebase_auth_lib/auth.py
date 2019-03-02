# Python Imports
import functools

# Flask Imports
from flask import request
from flask import abort

# Firebase Imports
import firebase_admin
from firebase_admin import auth, credentials

# JWT Imports
import jwt

cred = credentials.Certificate('firebase_auth_proj/keys/my-key.json')
default_app = firebase_admin.initialize_app(cred)


def verify_login(func):
    @staticmethod
    @functools.wraps(func)
    def wrapper():
        if not 'Authorization' in request.headers:
            abort(401)
        user = None
        token = request.headers['Authorization']
        try:
            decode_user = jwt.decode(token, verify=False, algorithms=['RS256'])['sub']
            try:
                auth.verify_id_token(token)
            except:
                abort(401)
            user = decode_user
        except:
            abort(401)
        return func(user)

    return wrapper


class MyFirebase(object):
    @staticmethod
    def user():
        if not 'Authorization' in request.headers:
            abort(401)
        token = request.headers['Authorization']
        decoded_token = auth.verify_id_token(token)
        user = {
            "email": decoded_token['email'],
            "user_id": decoded_token["user_id"],
            "auth_time": decoded_token["auth_time"],
            "email_verified": decoded_token['email_verified']
        }
        return user
