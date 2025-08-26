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


class Venue(Base):
    __tablename__ = "venues"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    Capacity = Column(Integer)
    participants = relationship("Participant", back_populates="venue")
    workshops = relationship("Workshop", back_populates="venue")

class Workshop(Base):
    __tablename__= "workshops"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text(200))
    organizer.id = Column(Integer, ForeignKey(organizer.id))
    venue.id = Column(Integer, ForeignKey("venue.id"))
    organizer = relationship("Organizer", back_populates="workshops")
    venue = relationship("Venue", back_populates="workshops")
