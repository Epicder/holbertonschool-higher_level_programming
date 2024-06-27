#!/usr/bin/python3
"""Module for the class Square"""

import sqlalchemy
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)


    session = sessionmaker(bind=engine)
    Session = session()
    for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
        print("{}: {}".format(state.id, state.name))
    Session.close()