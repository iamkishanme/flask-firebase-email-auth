from flask.views import MethodView


class ProfileAPI(MethodView):

    def get(self):
        return '<h1>Profile Detail</h1>'

    def post(self):
        return '<h1>Profile Create</h1>'

    def delete(self):
        return '<h1>Profile Delete</h1>'

    def put(self):
        return '<h1>Profile Update</h1>'
