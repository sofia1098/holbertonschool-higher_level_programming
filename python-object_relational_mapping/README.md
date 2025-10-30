Python-object_relational_mapping

Sintaxis Basica de ORM
# Ejemplo de definición de modelo
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)

Realizar consultas
Las consultas se construyen usando el objeto Query, que es generativo (cada método devuelve un nuevo objeto Query).
La cláusula WHERE se crea usando operadores de Python como == o != directamente en los objetos de columna, lo que genera expresiones SQL.
Para agrupar resultados, se usa el método group_by().
Para uniones, se puede utilizar joinedload() o externaljoin(). 
python
# Ejemplo de consulta de un usuario por ID
usuario = session.query(Usuario).filter(Usuario.id == 1).first()

# Ejemplo de búsqueda de usuarios de más de 25 años
usuarios_mayores = session.query(Usuario).filter(Usuario.edad > 25).all()
Insertar, actualizar y eliminar
Para insertar un nuevo objeto, se crea una instancia de la clase y se agrega a la sesión con session.add().
Para actualizar, se modifica el objeto existente y se confirma la sesión.
Para eliminar, se elimina el objeto de la sesión con session.delete() y luego se confirma. 
python
# Ejemplo de inserción de un nuevo usuario
nuevo_usuario = Usuario(nombre='Ana', edad=30)
session.add(nuevo_usuario)
session.commit()
