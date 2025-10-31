#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Crear el motor de conexión a la base de datos
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Crear la sesión para interactuar con la base de datos
    Session = sessionmaker(bind=engine)
    session = Session()

    # Consultar todos los estados, ordenados por id ascendente
    states = session.query(State).order_by(State.id).all()

    # Mostrar los resultados
    for state in states:
        print(f"{state.id}: {state.name}")

    # Cerrar la sesión
    session.close()
