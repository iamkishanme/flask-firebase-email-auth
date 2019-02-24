from flask import Blueprint

profile = Blueprint('auth', __name__)

from .views import ProfileAPI


profile_view = ProfileAPI.as_view('profile_api')

profile.add_url_rule('/', view_func=profile_view, methods=['GET','POST','PUT','DELETE'])
