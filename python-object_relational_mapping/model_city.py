#!/usr/bin/python3
"""Define a State city for SQLAlchemy ORM"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from model_state import Base

class City(Base):
    """City class that maps to the cities table"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, foreign_key=states.id)
