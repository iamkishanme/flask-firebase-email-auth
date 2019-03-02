# Flask Imports
from flask.views import MethodView

# Custom Lib Imports
from firebase_auth_proj.firebase_auth_lib.auth import verify_login, MyFirebase


class ProfileAPI(MethodView):

    def get(self):
        return '<h1>Profile Detail</h1>'

    @verify_login
    def post(self):
        user = MyFirebase.user()
        print(user)
        return '<h1>Profile Create</h1>'

    @verify_login
    def delete(self):
        user = MyFirebase.user()
        print(user)
        return '<h1>Profile Delete</h1>'

    @verify_login
    def put(self):
        user = MyFirebase.user()
        print(user)
        return '<h1>Profile Update</h1>'
