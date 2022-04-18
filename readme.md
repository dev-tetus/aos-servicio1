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
   
