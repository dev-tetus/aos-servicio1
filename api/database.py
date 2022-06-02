from flask_sqlalchemy import SQLAlchemy
from __main__ import app

config = {
    'host': 'db',
    'port': '3306',
    'user': 'root',
    'password': 'root',
    'database': 'trabajos'
}
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

# specify connection string
app.config['SQLALCHEMY_DATABASE_URI']= f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
db = SQLAlchemy(app)



def init_db():
    import schemas
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    db.create_all()

    #MODELOS!
    # import yourapplication.models