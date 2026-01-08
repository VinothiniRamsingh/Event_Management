from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import EventInfo
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
# from schemas import EventCreate 
from models import EventInfo
from schemas import EventCreate

EventInfo.metadata.create_all(bind=engine)

app = FastAPI(title="Event Management Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#  CREATE 
# @app.post("/events")
# def create_event(
#     booking_id: int,
#     user_name: str,
#     city: str,
#     phone: str,
#     event_type: str,
#     event_date: date,
#     location: str,
#     budget: int,
#     db: Session = Depends(get_db)
# ):
#     existing = db.query(EventInfo).filter(EventInfo.booking_id == booking_id).first()
#     if existing:
#         raise HTTPException(status_code=400, detail="Booking ID already exists")

#     event = EventInfo(
#         booking_id=booking_id,
#         user_name=user_name,
#         city=city,
#         phone=phone,
#         event_type=event_type,
#         event_date=event_date,
#         location=location,
#         budget=budget
#     )
#     db.add(event)
#     db.commit()
#     return {"message": "Event created successfully"}



@app.post("/events")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    # use event.user_name, event.city, etc.
    db_event = EventInfo(**event.dict())
    db.add(db_event)
    db.commit()
    return {"message": "Event created successfully"}

# @app.post("/events")
# def create_event(
#     user_name: str,
#     city: str,
#     phone: str,
#     event_type: str,
#     event_date: date,
#     location: str,
#     budget: int,
#     db: Session = Depends(get_db)
# ):
    
#     event = EventInfo(
#         user_name=user_name,
#         city=city,
#         phone=phone,
#         event_type=event_type,
#         event_date=event_date,
#         location=location,
#         budget=budget
#     )
#     db.add(event)
#     db.commit()
#     return {"message": "Event created successfully"}

#  READ ALL 
@app.get("/events")
def get_events(db: Session = Depends(get_db)):
    return db.query(EventInfo).all()

#  READ ONE 
@app.get("/events/{booking_id}")
def get_event(booking_id: int, db: Session = Depends(get_db)):
    event = db.query(EventInfo).filter(EventInfo.booking_id == booking_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

#  UPDATE 
@app.put("/events/{booking_id}")
def update_event(
    booking_id: int,
    user_name: str,
    city: str,
    phone: str,
    event_type: str,
    event_date: date,
    location: str,
    budget: int,
    db: Session = Depends(get_db)
):
    event = db.query(EventInfo).filter(EventInfo.booking_id == booking_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    event.user_name = user_name
    event.city = city
    event.phone = phone
    event.event_type = event_type
    event.event_date = event_date
    event.location = location
    event.budget = budget

    db.commit()
    return {"message": "Event updated successfully"}

#  DELETE 
@app.delete("/events/{booking_id}")
def delete_event(booking_id: int, db: Session = Depends(get_db)):
    event = db.query(EventInfo).filter(EventInfo.booking_id == booking_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(event)
    db.commit()
    return {"message": "Event deleted successfully"}
