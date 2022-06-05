from __main__ import app
from wsgiref.util import request_uri

from utils import utils as ut
from flask import Response
from flask import request
from sqlalchemy import exc


from controllers import controllerTrabajo

@app.route('/trabajo', methods=['GET', 'POST', 'OPTIONS'])
def trabajo():

    if request.method == 'GET':
        args = request.args

        # Llamar método de controllers pasando como argumento
        # el diccionario args para hacer el filtrado correcto
        # en funcion de los parametros

        return controllerTrabajo.cget_trabajo_controller(args)
    elif request.method == 'POST':
        try:
            response = controllerTrabajo.add_trabajo_controller(ut.parse_json(request.data))
            return response
        except exc.StatementError as e:
            if e.orig.args[0] == 1062:
                return Response(status=400, response='Datos duplicados')
            else:
                return str(e.orig)
    elif request.method == 'OPTIONS': 
       trabajoId

@app.route('/trabajo/<int:trabajoId>', methods=['GET', 'DELETE', 'PUT', 'OPTIONS'])
def trabajoId(trabajoId):

    if request.method == 'GET':
        try: 
            return controllerTrabajo.get_trabajo_controller(trabajoId)
        except Exception as e: 
            return str(e.__cause__)

    elif request.method == 'DELETE':
        return controllerTrabajo.delete_trabajo_controller(trabajoId)

    elif request.method == 'PUT':
        return controllerTrabajo.put_trabajo_controller(trabajoId,request)

    elif request.method == 'OPTIONS':
        return controllerTrabajo.optionsId_trabajo_controller(trabajoId)
