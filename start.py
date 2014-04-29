#encoding: utf-8

from application import app

#Debug flag, desactivar cuando se esté en  producción
app.debug = True

#Desde acá corre el programa.
if __name__ == '__main__':
	app.run()