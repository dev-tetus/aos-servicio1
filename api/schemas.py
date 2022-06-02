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
    return f"Trabajo(id={self.id!r}, vin={self.vin!r}, nombre={self.nombre!r}, descripcion={self.description!r}, fechaInicio={self.fechaInicio!r}, estado={self.estado!r}, matricula={self.matricula!r}, urgente={self.urgente!r})"


#Engine para la creación de conexiones con bases de datos, es una factoria.
#engine = create_engine("sqlite://", echo=True, future=True)
