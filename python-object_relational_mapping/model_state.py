#!/usr/bin/python3
"""Define a State class for SQLAlchemy ORM"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """State class that maps to the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")
