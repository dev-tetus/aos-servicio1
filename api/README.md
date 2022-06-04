# API Subsistema 3 de la práctica de especificación OpenAPI de la asignatura Arquitecturas Orientadas a Servicios.

# Instrucciones y Datos
- Integrar la imagen en el manifiesto como servicio.
- Este servicio se conecta a una base de datos MySQL (en la misma red de contenedores que este servicio)
- El servicio se encuentra en el puerto 5000 del contenedor
# Variables de entorno
- HOST
- DB_PASSWORD

En el manifiesto, será necesario añadir estas líneas para este servicio.
```
environment:
  HOST: <nombre_contenedor_mysql>
  DB_PASSWORD: <contraseña_usuario_root>
