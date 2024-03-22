#!/usr/bin/python3
"""
Creates the State "California"
City "San Francisco"
from the database hbtn_0e_100_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    added_State = State(name='California')
    added_City = City(name='San Francisco')
    added_State.cities.append(added_City)

    session.add(added_State)
    session.add(added_City)
    session.commit()
