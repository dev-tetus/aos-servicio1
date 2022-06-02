from flask import Flask

app = Flask(__name__)
import database as db
import routes #Registro de rutas

@app.route('/')
def index():
    return 'Hola!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'


if __name__ == '__main__':
    print('INICIANDO DB')
    db.init_db()
    app.run(debug=True, host='0.0.0.0')