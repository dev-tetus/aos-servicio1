# API Subsistema 3 de la práctica de especificación OpenAPI de la asignatura Arquitecturas Orientadas a Servicios.

# Instrucciones y Datos
- Integrar la imagen en el manifiesto como servicio.
- Este servicio se conecta a una base de datos MySQL (en la misma red de contenedores que este servicio)
- El servicio se encuentra en el puerto 5000 del contenedor
- El fichero docker-entrypoint.sh es el entrypoint de este servicio, corre en bucle a la espera de que el contenedor
de la base de datos esté listo
# Variables de entorno
- HOST
- DB_PASSWORD

En el manifiesto, será necesario añadir estas líneas para este servicio.
```
environment:
  HOST: <nombre_contenedor_mysql>
  DB_PASSWORD: <contraseña_usuario_root>
```

Un ejemplo de servicio de MySQL sería el siguiente:
```
mysql-db: 
    image: mysql
    container_name: db
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: trabajos
    volumes:
      - misDatos:/var/lib/mysql
    ports:
      - 6000:3306

volumes:
  misDatos
```

En este caso, en la declaración de este servicio quedaría:
```
environment:
  HOST: db
  DB_PASSWORD: root
```

