from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////web/Sqlite-Data/example.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()