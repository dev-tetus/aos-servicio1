from datetime import date
import enum
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class estadosTrabajo (enum.Enum):
    creado = "creado"
    planificado = "planificado"
    iniciado = "iniciado"
    termiando = "terminado"

class Trabajo(Base):
    __tablename__ = "trabajo"

    id = Column(Integer, primary_key=True)
    vin = Column(String(30))
    nombre = Column(String)
    descripcion = Column(String)
    fechaInicio = Column(date)
    estado = Column(enum.Enum(estadosTrabajo))
    matricula = Column(String)
    urgente = Column(bool)

#Terminar!!!!!
def __repr__(self):
    return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


#Engine para la creación de conexiones con bases de datos, es una factoria.
#engine = create_engine("sqlite://", echo=True, future=True)