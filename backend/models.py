from sqlalchemy import Column, Integer, String, Date
from database import Base
from pydantic import BaseModel
from datetime import date

from sqlalchemy import Column, Integer, String, Date
from database import Base

class EventInfo(Base):
    __tablename__ = "events_info"  # make sure this matches your table name in MySQL

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name  = Column(String(100), nullable=False)
    city       = Column(String(100), nullable=True)
    phone      = Column(String(20), nullable=True)
    event_type = Column(String(50), nullable=False)
    event_date = Column(Date, nullable=False)
    location   = Column(String(100), nullable=True)
    budget     = Column(Integer, nullable=True)


# class EventInfo(Base):
#     __tablename__ = "events_info"

#     booking_id = Column(Integer, primary_key=True, index=True)
#     user_name = Column(String(100), nullable=False)
#     city = Column(String(100), nullable=False)
#     phone = Column(String(15))
#     event_type = Column(String(50), nullable=False)
#     event_date = Column(Date, nullable=False)
#     location = Column(String(100), nullable=False)
#     budget = Column(Integer, nullable=False)


# class EventInfo(Base):
#     __tablename__ = "events_info"
#     booking_id = Column(Integer, primary_key=True, autoincrement=True)  # Auto increment
#     user_name = Column(String)
#     city = Column(String)
#     phone = Column(String)
#     event_type = Column(String)
#     event_date = Column(Date)
#     location = Column(String)
#     budget = Column(Integer)

