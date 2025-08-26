from sqlalchemy import Integer, String, Text, create_engine, Column, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

#Connect classes to the database using Base
Base = declarative_base 

class Organizer(Base):
    __tablename__ = "organizers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(40), nullable = False)
    last_name = Column(String(40), nullable = False)
    email_address = Column(String)
    phone_number = Column(Integer, nullable = False)
    workshops = relationship("Workshop", back_populates="organizer")



class participant(Base):
    __tablename__ = "participants"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    email_address = Column(String)
    phone_number = Column(Integer, nullable= False)
    venue.id = Column(Integer, ForeignKey(venue.id))
    workshops = relationship("Workshop", back_populates="participants")
    venue = relationship("Venue", back_populates="participants")

