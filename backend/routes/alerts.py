from fastapi import APIRouter, HTTPException
from models import AlertModel
from database import (
    get_all_alerts, get_alert_by_id, create_alert, update_alert, delete_alert
)

alert_router = APIRouter()

@alert_router.get("/api/alerts")
async def get_alerts():
    return await get_all_alerts() 

@alert_router.get("/api/alerts/{id}", response_model=AlertModel)
async def get_alert(id: str):
    alert = await get_alert_by_id(id)
    if not alert:
        raise HTTPException(status_code=404, detail=f"Alert with id {id} not found")
    return alert

@alert_router.post("/api/alerts", response_model=AlertModel)
async def save_alert(alert: AlertModel):
    response = await create_alert(alert.dict())
    if not response:
        raise HTTPException(status_code=400, detail="Error creating alert")
    return response

@alert_router.put("/api/alerts/{id}", response_model=AlertModel)
async def put_alert(id: str, alert: AlertModel):
    response = await update_alert(id, alert)
    if not response:
        raise HTTPException(status_code=404, detail=f"Alert with id {id} not found")
    return response

@alert_router.delete("/api/alerts/{id}")
async def remove_alert(id: str):
    response = await delete_alert(id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Alert with id {id} not found")
    return {"message": "Alert deleted successfully"}