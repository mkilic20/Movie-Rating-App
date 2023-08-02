from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from .database import Base
from typing import Optional

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True)
    hashed_password = Column(String(255), unique=True)
    

class Movie(Base):
    __tablename__ = "movies"

    MovieID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Name = Column(String(255), unique=True)
    Year = Column(Integer)
    Runtime = Column(Integer)
    Rating = Column(Float)
    Votes = Column(Integer)
    Revenue = Column(Float, nullable=True)


    