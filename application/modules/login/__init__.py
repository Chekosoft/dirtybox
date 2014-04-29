#encoding: utf-8

from application import app
from ..base.models import User, LoggedUser
from flask_login import LoginManager, login_required
from peewee import DoesNotExist

from flask import request, url_for, Blueprint

#Definiendo que parte maneja el login de usuario
login_manager = LoginManager(app)
login_manager.login_view = 'login.do_login'

login_module = Blueprint('login', __name__, template_folder='templates')

@login_manager.user_loader
def load_user(user_id):
	try:
		user = User.get(User.id==user_id)
		logged_user = LoggedUser()
		logged_user.user_id = user.id
		logged_user.is_active = user.is_active
		return logged_user

	except DoesNotExist:
		return None

@login_module.route('/do_login', methods=['GET', 'POST'])
def do_login():
	if request.method == 'GET':
		return u'No hay problema, Willy'

app.register_blueprint(login_module, url_prefix='/login')