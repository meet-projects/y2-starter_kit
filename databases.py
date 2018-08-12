# Database related imports
# Make sure to import your tables!
from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_user(name, passwd):
    sess = DBSession()

    check = sess.query(User).filter_by(username=name).first()
    if check is not None:
        raise RegException()

    user = User(username=name, password=passwd)
    sess.add(user)
    sess.commit()

def auth_user(name, passwd):
    sess = DBSession()
    check = sess.query(User).filter_by(username=name, password=passwd).first()

    return check is not None

class RegException(Exception):
    pass