'''
Sqlalchemy(ORM) with data mapper and Declarative
pip install sqlalchemy

components in ORM
1. Table ->table in db
2. A mapper that maps python class to table in db (ORM)
3. class object that defines how db record maps to pyhton object

CRUD

already existing tables means connect it and use it . 
else declare  the table like below example
'''

import os, sys
from sqlalchemy import Column,ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base() #base model --something like abstract class, base metadata

class Person(Base): #model class python class/object
    __tablename__='person' #in db table name
    id=Column(Integer,primary_key=True)
    name=Column(String(250),nullable=False)

class Address(Base):
    __tablename__='address'
    id=Column(Integer,primary_key=True)
    city=Column(String(50))
    post_code=Column(String(10),nullable=False)
    person_id=Column(Integer,ForeignKey("person.id"))
    person=relationship(Person)

engine=create_engine('sqlite:///boa.db') #sqllite will not have any port number anything whereas other serveres they require all these details
#create all tables from ORM create table person.....,create table address
Base.metadata.create_all(engine)
#tables will be created

print("BOA db tables created")
# the db can be seen through sqllitebrowser.org

