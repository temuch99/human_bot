from sqlalchemy import Integer, String, Column, Unicode, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    """
    Table with active users
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, nullable=False)

class Human(Base):
    """
    Table with humans
    """
    __tablename__ = 'human'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    surname = Column(String(50), nullable=True)
    birthdate = Column(Date(), nullable=True)
    other = Column(Unicode(200))

class Organization(Base):
    """
    Table with organizations
    """
    __tablename__ = 'organization'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    type = Column(String(50), nullable=True)
    inn = Column(Integer, nullable=True)
    other = Column(Unicode(200))
