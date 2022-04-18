const express = require('express')
const swaggerUi =require('swagger-ui-express')
const document = require('./api/swagger')




const app = express()

app.use('/api/',swaggerUi.serve, swaggerUi.setup(document))

const PORT = 3000
app.listen(PORT, () =>{
    console.log(`Listening on port ${PORT}`);
})