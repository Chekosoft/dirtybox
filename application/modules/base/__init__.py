#encoding: utf-8

"""
El módulo base solo define 
los modelos de datos para el usuario y las transacciones del sistema.
Además, define el módulo usado para verificar si el usuario inició sesión
en el sistema.
"""

from application import app
import peewee

#Acá definimos las conexiones a la base de datos.

dbproxy = peewee.Proxy()
db = None

if app.debug == True:
	db = peewee.SqliteDatabase('../../data/debug.sqlite')
else:
	#FIXME: tratar de cambiar por otro motor
	db = peewee.SqliteDatabase('../../data/production.sqlite')

dbproxy.initialize(db)