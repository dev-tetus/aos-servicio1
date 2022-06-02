from re import M
from database import db
from schemas import Trabajo
from flask import Response
import json

params = ['page','id','order']

def get_trabajo_controller(args):
    query_params = {}
    if len(args) > 0:
        for arg in args:
            if arg not in params:
                return Response(status=400, response='Invalid params')
            query_params[arg] = args[arg]
    
        trabajo = Trabajo.query.all()
        return str(trabajo)
    else:
        trabajos = Trabajo.query.all()
        return str(trabajos)
        

def add_trabajo_controller(params):
    query_params = {}
    if len(params) > 0:
        trabajo = Trabajo(params)
        db.session.add(trabajo)
        db.session.commit()
        return str(trabajo)
        return trabajo.__repr__()
        return Response(status=200, response='Creado')
    else:
        return params
