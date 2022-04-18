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

# Docker
### 1. Directorio
```bash
cd susbsistema_3
```
### 2. Construcción de la imagen
```bash 
docker build -t <subsistema_3>
```
### 3. Levantar contenedor
```bash
docker run -p <puerto_deseado>:3000 <subsistema_3>
```
### 4. Navegador
```bash
http://localhost:<puerto_deseado>/api/
```
   [swagger-ui-express]: <https://www.npmjs.com/package/swagger-ui-express>
   
