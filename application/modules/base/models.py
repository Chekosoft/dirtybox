#encoding: utf-8

#Importamos referencia al objeto aplicación para ver si estamos en debug mode.
from application import app
#Peewee!
import peewee

db = None

if app.debug == True:
	db = peewee.SqliteDatabase('../../data/debug.sqlite')
else:
	#FIXME: tratar de cambiar por otro motor
	db = peewee.SqliteDatabase('../../data/production.sqlite')

#Para que no se vaya a la B la conexión a la base de datos.
assert(db is not None)

#Modelo base.
class BaseModel(peewee.Model):
	class Meta:
		database = db

#Modelo de usuario.
class User(BaseModel):
	uid = peewee.PrimaryKeyField()
	name = peewee.CharField()
	is_admin = peewee.BooleanField(default=False)

	class Meta:
		indexes = (('name'), True)

