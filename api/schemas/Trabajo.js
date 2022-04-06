const link = require('./Link')
module.exports = {
  "description": "Información de un trabajo",
  "title": "🔨 Trabajo",
  "type": "object",
  "properties": {
    "game": {
      "type": "object",
      "required": [
        "nombre",
        "descripcion",
        "fechaInicio",
        "estado"
      ],
      "properties": {
        "id": {
          "type": "integer",
          "format": "int32",
          "description": "Id trabajo",
          "readOnly": true
        },
        "nombre": {
          "description": "Nombre del trabajo",
          "type": "string"
        },
        "descripcion": {
          "description": "Descripción del trabajo",
          "type": "string"
        },
        "fechaInicio": {
          "description": "Indica la fecha de inicio del trabajo",
          "type": "string"
        },
        "estado": {
          "description": "Estado del trabajo de entre cuatro opciones",
          "type": "string",
          "enum": [
            "creado",
            "planificado",
            "iniciado",
            "terminado"
          ]
        },
        "matricula": {
          "description": "Número de matrícula del vehículo en el cual se va a realizar el trabajo",
          "type": "string"
        },
        "urgente": {
          "description": "Dice si el trabajo es urgente",
          "type": "boolean",
          "default": false
        },
        "links": {
          "description": "Enlaces de relación",
          "readOnly": true,
          "type": "object",
          "properties": {
            "parent": link,
            "self": link,
          }
        }
      }
    }
  },
  "example": {
    "trabajo-example": {
      "value": null,
      "trabajo": {
        "id": 789,
        "nombre": "Cambio de aceite",
        "descripcion": "Cambio de aceite",
        "fechaInicio": "15-04-2022",
        "estado": "planificado",
        "matricula": "5677JJYP",
        "urgente": true,
        "links": {
          "parent": {
            "href": "https://example.com/api/v1/trabajo",
            "rel": "listaTrabajos"
          },
          "self": {
            "href": "https://example.com/api/v1/trabajo/2022",
            "rel": "obtenerTrabajo modificarTrabajo eliminarTrabajo"
          }
        }
      }
    }
  }
}