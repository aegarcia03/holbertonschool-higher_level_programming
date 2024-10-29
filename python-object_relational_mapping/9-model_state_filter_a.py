#!/usr/bin/python3
"""Lists the first object from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()  # Start a session

    a_state = session.query(State).filter(State.name.like('%a%'))
    for state in a_state:
        print(f'{state.id}: {state.name}')

    session.close()
