from database import db
from schemas import Trabajo
from flask import Response
import json

paramsCget = ['page','id','order']

#Metodos de la ruta /trabajo

def cget_trabajo_controller(args):
    query_params = {}
    if len(args) > 0:
        for arg in args:
            if arg not in paramsCget:
                return Response(status=400, response='Invalid params')
            query_params[arg] = args[arg]
    
        trabajo = Trabajo.query.all()
        return str(trabajo)
    else:
        trabajos = Trabajo.query.all()
        return str(trabajos)
        

def add_trabajo_controller(params):
    if len(params) > 0:
        trabajo = Trabajo(params)
        db.session.add(trabajo)
        db.session.commit()
        return Response(status=200, response='Creado')
    else:
        return Response(status=400, response="Datos vacíos")

def options_trabajo_controller ():
    pass

#Metodos de la ruta /trabajo/{trabajoId}

def get_trabajo_controller(args):
    print(args)
    #if len(args) == 1:
       # trabajo = Trabajo.query.get_or_404(trabajo_id)
        #return str(trabajo)  
   # else: 
       # return Response(status=400, response='Invalid params')

def delete_trabajo_controller(trabajo_id):
    trabajo = Trabajo.query.get_or_404(trabajo_id)
    db.session.delete(trabajo)
    db.session.commit()
    return Response(status = 204, response='Trabajo borrado')
        
def optionsId_trabajo_controller ():
    pass

def put_trabajo_controller ():
    pass