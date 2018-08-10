# Database related imports
# Make sure to import your tables!
from model import Base, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_student(name, year):
    student = Student(name = name, year = year)
    session.add(student)
    session.commit()

def query_all():
    return session.query(Student).all()

def query_filtered(**kwargs):
    return session.query(Student).filter_by(**kwargs).all()


# add_student("Matt", 2)
# add_student("Shira", 1)
# add_student("Badea", 3)
# add_student("Eilon", 2)
# add_student("Yair", 1)

print(query_filtered(name="Badea"))