#!/usr/bin/python3
"""A script that prints the first State object from database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    record = session.query(State).first()

    if record:
        print("{}: {}".format(record.__dict__['id'], record.__dict__['name']))
    else:
        print("Nothing")

    session.close()
