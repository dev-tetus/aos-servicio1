# Subsistema 3 de la práctica de especificación OpenAPI de la asignatura Arquitecturas Orientadas a Servicios.
### __Información integrantes__

| Nombre y apellidos | Matrícula | Correo |
| ------ | ------ | ------ |
| Teófilo Roca Miralles | bp0481 | t.roca@alumnos.upm.es |
| Álvaro Avilés Redondo | bp0259 | alvaro.avilesr@alumnos.upm.es |
| Fabián Magro Del Pozo | bp0260 | fabian.magro.delpozo@alumnos.upm.es |
| Cristian Chelemen | bp0228 | cristian.chelemen@alumnos.upm.es |

Para levantar el servicio, hemos decidio utilizar Express como servidor web a través del cual se muestra la especificación del servicio.
- Utilizamos el módulo [swagger-ui-express] de Node que ofrece la posibilidad de servir la especificación a través de un fichero JSON.
- Para la separación de los esquemas, a través de la creación de módulos con la sentencia _module.exports_, devolvemos objetos JSON los cuales serán inyectados en el fichero principal en su lugar correspondiente.

*Nota: hemos entregado los ficheros de la especificación también en formato YAML (se encuentran tanto en este repositorio, como entregados junto con el readme.txt que se adjunta en la entrega de moodle de la práctica). Aparte de esto se encuentran en formato JS para poder levantar el swagger UI con la especificación (siguiendo los pasos que se detallan debajo).

# Git 
Primero se debe clonar el repositorio en local 
```bash
git clone https://github.com/dev-tetus/susbsistema_3.git
```
# Docker
### 1. Directorio
Abrimos una consola en la ubicación de la carpeta que hemos clonado: susbsistema_3
```bash
cd susbsistema_3
```
### 2. Construcción de la imagen
```bash 
docker build -t subsistema_3 .
```
### 3. Levantar contenedor
Debemos asegurarnos primero que el puerto 80 está libre, en otro caso dejarlo libre o indicar otro puerto
```bash
docker run -p 80:3000 subsistema_3
```
### 4. Navegador
Pegar en el navegador la siguiente URL (si se ha cambiado el puerto en el paso 3, cambiar el 80 por el puerto usado)
```bash
http://localhost:80/api/
```
   [swagger-ui-express]: <https://www.npmjs.com/package/swagger-ui-express>
   

# Parte 2

Para la implementación con docker-compose, utilizamos una imagen de un servidor nginx que actúa como enrutador de servicios,
para levantar estos contenedores habría que jecutar los siguientes comandos:
```bash
cd k8
```
```bash
docker-compose up --build -d
```
- La especificación de la API será accesible desde http://localhost/
- Los endpoints de la API desde http://localhost/api
- La interfaz para controlar la base de datos desde http://localhost/db

Para la implementación de los servicios en Kubernetes, hemos decidido contratar un cluster en Digital Ocean, de 1 nodo.
Hemos creado un solo manifiesto en el que se declaran todos los Deployment, Services y PersitentVolumes utilizados por 
nuestro sistema.

```bash
export KUBECONFIG=<ruta_fichero>
```
Los servicios quedan activos de tal manera que se pueda mantener la ip del servicio encargado de ser el punto de entrada
como un API Gateway en el cluster mientras que los pods serán creados por los profesores de la asignatura con el fin de 
probar el sistema.

Para eliminar los Deployment con el fin de generar nuevos pods como Deployment, es necesario ejecutar este comando primero
```bash
kubectl delete --all deployments --namespace=default
```
A continuación
```bash
kubectl apply -f aos-deployment-production.yaml
```

- La interfaz para controlar la base de datos desde http://139.59.200.221/db/
- La especificación de la API de trabajos será accesible desde http://139.59.200.221/
- La api del sistema de trabajos desde http://139.59.200.221/api
- La api del sistema de facturas desde http://139.59.200.221/facturas
- La api del sistema de facturas dos desde http://139.59.200.221/facturas-dos
- La api del sistema de notificaciones desde http://139.59.200.221/notificaciones
- La api del sistema de vehiculos desde http://139.59.200.221/vehiculos
- La api del sistema de vehiculos-dos desde http://139.59.200.221/vehiculos-dos
- La api del sistema de logs desde http://139.59.200.221/logs
- La api del sistema de recambios desde http://139.59.200.221/recambios
