#encoding: utf-8

"""
	Definición de modelos base para la extensión de módulos de la caja sucia
"""

#Importamos referencia al objeto aplicación para ver si estamos en debug mode.
from application import app
#Importamos un objeto de ayuda para generara más fácil el usuario.
from flask_login import UserMixin
#Peewee!
import peewee
from ..base import dbproxy

"""
Modelo base para todas las entidades de la caja sucia.
"""
class BaseModel(peewee.Model):
	class Meta:
		database = dbproxy

"""
Modelo que representa un usuario del sistema.
"""
class User(BaseModel):
	#ID del usuario dentro del sistema.
	id = peewee.PrimaryKeyField()
	#Login del usuario (ej: joaquin.munoz)
	login = peewee.CharField()
	#Nombre del usuario (ej: Cheko)
	name = peewee.CharField()
	#¿Es administrador del sistema?
	is_admin = peewee.BooleanField(default=False)
	#Está activo en el sistema?
	is_active = peewee.BooleanField(default=True)

	class Meta:
		indexes = (('login'), True) #Los login son únicos.

"""
Modelo que representa una transacción dentro del sistema.
"""
class Transaction(BaseModel):
	#Id de transacción.
	id = peewee.PrimaryKeyField()
	#El usuario del sistema que generó la transacción.
	generator = peewee.ForeignKeyField(User, related_name='transactions')
	#El valor de la transacción realizada (puede ser negativo para préstamos)
	transaction_value = peewee.FloatField()
	#El total de la caja.
	accumulated_value = peewee.FloatField()

"""
Cuando se inicia sesión, éste es el token que el usuario obtiene.
"""
class LoggedUser(UserMixin):

	user_id = None
	is_active = False

	def is_authenticated(self):
		return self.user_id is not None

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.userid)

	def is_active(self):
		return self.is_active