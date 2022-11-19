import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from os.path import abspath, dirname

DATABASE_URL = "postgresql://temuch:bander04log@localhost/mng"

engine = sqlalchemy.create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
