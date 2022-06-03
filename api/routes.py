from __main__ import app

from utils import utils as ut
from flask import Response
from flask import request
from sqlalchemy import exc


from controllers import controllerTrabajo

@app.route('/trabajo', methods=['GET', 'POST'])
def trabajo():

    if request.method == 'GET':
        args = request.args

        # Llamar método de controllers pasando como argumento
        # el diccionario args para hacer el filtrado correcto
        # en funcion de los parametros

        return controllerTrabajo.get_trabajo_controller(args)
    else:
        try:
            response = controllerTrabajo.add_trabajo_controller(ut.parse_json(request.data))
            return response
        except exc.StatementError as e:
            if e.orig.args[0] == 1062:
                return Response(status=400, response='Datos duplicados')
            else:
                return str(e.orig)

