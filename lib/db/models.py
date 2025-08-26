from sqlalchemy import Integer, String, Text, create_engine, Column, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

#Connect classes to the database using Base
Base = declarative_base 
