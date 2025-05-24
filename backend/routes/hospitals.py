from fastapi import APIRouter, HTTPException
from models import HospitalModel
from database import (
    get_all_hospitals, get_hospital_by_id, create_hospital, update_hospital, delete_hospital
)

hospital_router = APIRouter()

@hospital_router.get("/api/hospitals")
async def get_hospitals():
    return await get_all_hospitals()

@hospital_router.get("/api/hospitals/{id}", response_model=HospitalModel)
async def get_hospital(id: str):
    hospital = await get_hospital_by_id(id)
    if not hospital:
        raise HTTPException(status_code=404, detail=f"Hospital with id {id} not found")
    return hospital

@hospital_router.post("/api/hospitals", response_model=HospitalModel)
async def save_hospital(hospital: HospitalModel):
    response = await create_hospital(hospital.dict())
    if not response:
        raise HTTPException(status_code=400, detail="Error creating hospital")
    return response

@hospital_router.put("/api/hospitals/{id}", response_model=HospitalModel)
async def put_hospital(id: str, hospital: HospitalModel):
    response = await update_hospital(id, hospital)
    if not response:
        raise HTTPException(status_code=404, detail=f"Hospital with id {id} not found")
    return response

@hospital_router.delete("/api/hospitals/{id}")
async def remove_hospital(id: str):
    response = await delete_hospital(id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Hospital with id {id} not found")
    return {"message": "Hospital deleted successfully"}
