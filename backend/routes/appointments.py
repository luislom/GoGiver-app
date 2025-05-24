from fastapi import APIRouter, HTTPException
from fastapi import FastAPI
from models import AppointmentModel, AppointmentUpdateModel
from database import (
    get_all_appointments, get_appointment_by_id, create_appointment, update_appointment, delete_appointment
)
appointment_router = APIRouter()


@appointment_router.get("/api/appointments")
async def get_appointments():
    return await get_all_appointments()

@appointment_router.get("/api/appointments/{id}", response_model=AppointmentModel)
async def get_appointment(id: str):
    appointment = await get_appointment_by_id(id)
    if not appointment:
        raise HTTPException(status_code=404, detail=f"Appointment with id {id} not found")
    return appointment

@appointment_router.post("/api/appointments", response_model=AppointmentModel)
async def save_appointment(appointment: AppointmentModel):
    response = await create_appointment(appointment.dict())
    if not response:
        raise HTTPException(status_code=400, detail="Error creating appointment")
    return response

@appointment_router.put("/api/appointments/{id}", response_model=AppointmentModel)
async def put_appointment(id: str, appointment: AppointmentUpdateModel):
    response = await update_appointment(id, appointment)
    if not response:
        raise HTTPException(status_code=404, detail=f"Appointment with id {id} not found")
    return response

@appointment_router.delete("/api/appointments/{id}")
async def remove_appointment(id: str):
    response = await delete_appointment(id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Appointment with id {id} not found")
    return {"message": "Appointment deleted successfully"}
