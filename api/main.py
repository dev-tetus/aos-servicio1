from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
import database as db
import routes #Registro de rutas

@app.route('/')
def index():
    return 'Hola!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'


if __name__ == '__main__':
    print('INICIANDO DB')
    db.init_db()
    app.run(debug=True, host='0.0.0.0')