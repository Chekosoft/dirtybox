#encoding: utf-8

from application import app
import config 

#Debug flag, desactivar cuando se esté en  producción
app.debug = True
app.config['dirtybox'] = config.parameters
app.secret_key = app.config['dirtybox']['secret_key']


#Desde acá corre el programa.
if __name__ == '__main__':
	app.run()