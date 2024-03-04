from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(
    tags=["Events"]
)

events=[]

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    print(f"events : {events}")
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_events(id: int) -> Event:
    for event in events:
        if event.id==id:
            return event
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    print(f"new event : {body}")
    events.append(body)
    return {
        "message": "Event created successfully."
    }

@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        print(f"remove event : {event}")
        events.remove(event)
        return {
            "message" : "Event deleted successfully."
        }

@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message":"Events deleted successfully."
    }        