from fastapi import APIRouter, HTTPException
from models import NotificationModel
from database import (
    get_all_notifications, get_notification_by_id, create_notification, update_notification, delete_notification
)

notification_router = APIRouter()

@notification_router.get("/api/notifications")
async def get_notifications():
    return await get_all_notifications()

@notification_router.get("/api/notifications/{id}", response_model=NotificationModel)
async def get_notification(id: str):
    notification = await get_notification_by_id(id)
    if not notification:
        raise HTTPException(status_code=404, detail=f"Notification with id {id} not found")
    return notification

@notification_router.post("/api/notifications", response_model=NotificationModel)
async def save_notification(notification: NotificationModel):
    response = await create_notification(notification.dict())
    if not response:
        raise HTTPException(status_code=400, detail="Error creating notification")
    return response

@notification_router.put("/api/notifications/{id}", response_model=NotificationModel)
async def put_notification(id: str, notification: NotificationModel):
    response = await update_notification(id, notification)
    if not response:
        raise HTTPException(status_code=404, detail=f"Notification with id {id} not found")
    return response

@notification_router.delete("/api/notifications/{id}")
async def remove_notification(id: str):
    response = await delete_notification(id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Notification with id {id} not found")
    return {"message": "Notification deleted successfully"}