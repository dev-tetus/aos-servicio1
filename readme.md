[H2]1.- Construir imagen
docker build -t <nombre_imagen> .
[H2]2.- Correr imagen
docker run [-d] -p<puerto_deseado>:3000 <nombre_imagen>
