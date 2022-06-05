from sqlalchemy import null
from database import db
from schemas import Trabajo
from flask import Response, make_response
import json
import datetime as dt

paramsCget = ['page','id','order']

#Metodos de la ruta /trabajo

def cget_trabajo_controller(args): #CAMBIAR EL METODO DE __repr__ para que no saque solo un string, darle algo de forma.
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
    return Response(status = 204, headers = [("Allow" , ["GET", "POST", "OPTIONS"])])

#Metodos de la ruta /trabajo/{trabajoId}

def get_trabajo_controller(trabajo_id):
    if trabajo_id is not null:
        trabajo = Trabajo.query.get(trabajo_id)
        if trabajo is None:
            return Response(status = 404, response='Not found')
        else:
            response = make_response(trabajo.__repr__())
            response.add_etag()
            return response
    else: 
       return Response(status=400, response='Invalid params')

def delete_trabajo_controller(trabajo_id):
    trabajo = Trabajo.query.get(trabajo_id)
    if trabajo is None:
        return Response(status = 404, response='Not found')
    else:
        db.session.delete(trabajo)
        db.session.commit()
        return Response(status = 204, response='Trabajo borrado')
        
def optionsId_trabajo_controller(trabajo_id):
    trabajo = Trabajo.query.get(trabajo_id)
    if trabajo is None:
        return Response(status = 204,  headers = [("Allow", [])])
    else:
        return Response(status = 204, headers = [("Allow", ["GET", "DELETE", "OPTIONS", "PUT"])])


def put_trabajo_controller(trabajo_id,request):
    trabajo_response = get_trabajo_controller(trabajo_id)

    if trabajo_response._status_code == 404:
        return Response(status = 404, response='Not found') 

    elif str('"'+request.headers.get('If-Match')+'"') == str(trabajo_response.headers.get('etag')):
        request.json['fechaInicio'] = dt.datetime.strptime(request.json['fechaInicio'],'%d-%m-%Y')
        trabajo = Trabajo.query.filter_by(id=trabajo_id)
        trabajo.update(request.json)

        # trabajo = Trabajo(request.json)

        
        # trabajo.VIN = request.json['VIN']
        # trabajo.nombre = request.json['nombre']
        # trabajo.descripcion = request.json['descripcion']
        # trabajo.fechaInicio = dt.datetime.strptime(request.json['fechaInicio'],'%d-%m-%Y')
        # trabajo.estado = request.json['estado']
        # trabajo.matricula = request.json['matricula']
        # trabajo.urgente = bool(request.json['urgente'])
        db.session.commit()

        return Response(status=200, response=Trabajo.query.get(trabajo_id).__repr__())
    else:
        return Response(status=412, response='Precondition failed: ETAG proporcionado no está actualizado')
        


    # if 'abbr' in request.json:
    #     station.abbr = request.json['abbr']
    # if 'name' in request.json:
    #     station.name = request.json['name']
    # if 'gtfs_latitude' in request.json:
    #     station.gtfs_latitude = request.json['gtfs_latitude']
    # if 'gtfs_longitude' in request.json:
    #     station.gtfs_longitude = request.json['gtfs_longitude']
    # if 'address' in request.json:
    #     station.address = request.json['address']
    # if 'city' in request.json:
    #     station.city = request.json['city']
    # if 'county' in request.json:
    #     station.county = request.json['county']
    # if 'state' in request.json:
    #     station.state = request.json['state']
    # if 'zipcode' in request.json:
    #     station.zipcode = request.json['zipcode']
        
    # db.session.commit()
    # return station_schema.dump(station)