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

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f'{first_state.id}: {first_state.name}')
    else:
        print("No data")

    session.close()
