const express = require('express')
const swaggerUi =require('swagger-ui-express')
// const YAML = require('yamljs')
const document = require('./api/swagger')
// const document1 = YAML.load('./api/schemas/HTTP_Problem.yaml')
// const document2 = YAML.load('./api/schemas/Link.yaml')
// const document3 = YAML.load('./api/schemas/Trabajo.yaml')



const app = express()

app.use('/api/',swaggerUi.serve, swaggerUi.setup(document))

const PORT = 3000
app.listen(PORT, () =>{
    console.log(`Listening on port ${PORT}`);
})