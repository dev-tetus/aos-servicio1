from flask import Flask

import database as db
app = Flask(__name__)
import routes #Registro de rutas

@app.route('/')
def index():
    return 'Hola!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

@app.route('/trabajo')
def get_trabajo():
    return 'Trabajo'

if __name__ == '__main__':
    print('INICIANDO DB')
    db.init_db()
    app.run(debug=True, host='0.0.0.0')