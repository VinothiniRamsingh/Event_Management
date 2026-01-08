from pydantic import BaseModel
from datetime import date

class EventCreate(BaseModel):
    user_name: str
    city: str
    phone: str
    event_type: str
    event_date: date
    location: str
    budget: int