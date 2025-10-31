#!/usr/bin/python3
""" Print the State id with the name passed as argument """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # filter (prevents injection)
    state = session.query(State).filter(State.name == search_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
