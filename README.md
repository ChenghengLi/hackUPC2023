#  Software para optimizar el rendimeinto de los estduios utlizando la IA


SPA: Single-page application, más información en https://es.wikipedia.org/wiki/Single-page_application

### Creador: Chengheng Li Chen, Wenwen Yang, Xu Yao Chen y Zhihan Lin 

## Frontend

El frontend está desarrolado con el framework de Vue.js + Vue CLI, donde se puede encontrar la documentación en la siguiente página https://vuejs.org/guide/quick-start.html#using-vue-from-cdn

Se puede usar la estructura de <script setup> para la optimización de los recursos, junto el plugin de Axios, después de injectarlo en cada componente.
  
Estña vinvulado a http://localhost:8080/
## Backend

El backend el backend estña desarrolado con FastApi, que se puede encontrar la documentación en el siguiente enlace https://fastapi.tiangolo.com/
  
Estña vinvulado a http://localhost:5000

## Run en Docker toda la apliación Frontend + Backend
  
Ejecutar el siguiente comando en la carpeta raíz después de abrir Docker Desktop:
```
docker-compose up -d --build
```
Para ver el resultado de la pñagina web se podrña acceder a: http://localhost:8080/

## Run sólo el FrontEnd para el proceso de desarrllo

Intalar node.js en el caso de que no lo tenga: https://nodejs.org/es
 
Ejecutar la siguiente línia la primera vez en el nivel de la carpeta de Frontend
```
npm install
```
Ejecutar el siguiente comando para compilar y ver el resultado
  
```
npm run serve
```

