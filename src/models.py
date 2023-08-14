import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ ='user'
    id = Column(Integer,primary_key = True)
    name = Column(String(40),nullable = False)
    email= Column(String(60),nullable = False)
    password = Column(String(90),nullable =False)


class Planets(Base):
    __tablename__ ='planet'
    id = Column(Integer,primary_key = True)
    name = Column(String(30),nullable = False)
    terrain = Column(String(40),nullable = False)
    gravity = Column(String(110),nullable =False)

class Chararacters(Base):
    __tablename__ = 'characters'
    id = Column(Integer,primary_key = True)
    name = Column(String(30),nullable = False)
    hair_color = Column(String(40),nullable = False)
    birth_year = Column(String(110),nullable =False)
    eye_color = Column(String(50),nullable= False)


class Favorites(Base):
    __tablename__='favorites'
    id = Column(Integer,primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planet.id'))
    chararacters_id = Column(Integer, ForeignKey('characters.id'))
    chararacters= relationship(Chararacters)
    planets= relationship(Planets)
    user =relationship(User)

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    na = Column(String(250), nullable=False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
