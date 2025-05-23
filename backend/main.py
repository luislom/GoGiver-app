from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
from database import (
    get_all_users, create_user, get_user_by_name, get_user_by_id, update_user, delete_user,
    get_all_appointments, get_appointment_by_id, create_appointment, update_appointment, delete_appointment,
    get_all_alerts, get_alert_by_id, create_alert, update_alert, delete_alert,
    get_all_donations, get_donation_by_id, create_donation, update_donation, delete_donation,
    get_all_hospitals, get_hospital_by_id, create_hospital, update_hospital, delete_hospital,
    get_all_notifications, get_notification_by_id, create_notification, update_notification, delete_notification
)
from models import (
    UserModel, UserUpdateModel, AppointmentModel, AlertModel, DonationModel, HospitalModel, NotificationModel, AppointmentUpdateModel
)

app = FastAPI()



@app.get("/")

def welcome():
    return {"message":"Welcome to GoGiver App"}


@app.get("/api/users")
async def get_users():
    users = await get_all_users() 
    return users


@app.post("/api/users", response_model=UserModel)
async def save_user(user: UserModel):
    userFound =await get_user_by_name(user.full_name)
    if userFound:
        raise HTTPException(status_code=400, detail="User already exists")
    
    response = await create_user(user.dict())
    if not response:
        raise HTTPException(status_code=400, detail="Error creating user")
    return response

@app.get("/api/users/{id}", response_model=UserModel)
async def get_user(id: str):
    user = await get_user_by_id(id)
    if not user: 
        raise HTTPException(status_code=404, detail="User with id {id} not found")
    return user


@app.put("/api/users/{id}", response_model=UserModel)
async def put_user(id: str, user: UserUpdateModel):
    response = await update_user(id, user)
    if not response:
        raise HTTPException(status_code=404, detail="User with id {id} not found")
    return response


@app.delete("/api/users/{id}")
async def remove_user(id: str): 
    response = await delete_user(id)
    if not response:
        raise HTTPException(status_code=404, detail="User with id {id} not found") 
    return {"message": "User deleted successfully"}


# APPOINTMENTS
@app.get("/api/appointments")
async def get_appointments():
    return await get_all_appointments()

@app.get("/api/appointments/{id}", response_model=AppointmentModel)
async def get_appointment(id: str):
    appointment = await get_appointment_by_id(id)
    if not appointment:
        raise HTTPException(status_code=404, detail=f"Appointment with id {id} not found")
    return appointment

@app.post("/api/appointments", response_model=AppointmentModel)
async def save_appointment(appointment: AppointmentModel):
    response = await create_appointment(appointment.dict())
    if not response:
        raise HTTPException(status_code=400, detail="Error creating appointment")
    return response

@app.put("/api/appointments/{id}", response_model=AppointmentModel)
async def put_appointment(id: str, appointment: AppointmentUpdateModel):
    response = await update_appointment(id, appointment)
    if not response:
        raise HTTPException(status_code=404, detail=f"Appointment with id {id} not found")
    return response

@app.delete("/api/appointments/{id}")
async def remove_appointment(id: str):
    response = await delete_appointment(id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Appointment with id {id} not found")
    return {"message": "Appointment deleted successfully"}


# ALERTS
@app.get("/api/alerts")
async def get_alerts():
    return await get_all_alerts() 

@app.get("/api/alerts/{id}", response_model=AlertModel)
async def get_alert(id: str):
    alert = await get_alert_by_id(id)
    if not alert:
        raise HTTPException(status_code=404, detail=f"Alert with id {id} not found")
    return alert

@app.post("/api/alerts", response_model=AlertModel)
async def save_alert(alert: AlertModel):
    response = await create_alert(alert.dict())
    if not response:
        raise HTTPException(status_code=400, detail="Error creating alert")
    return response

@app.put("/api/alerts/{id}", response_model=AlertModel)
async def put_alert(id: str, alert: AlertModel):
    response = await update_alert(id, alert)
    if not response:
        raise HTTPException(status_code=404, detail=f"Alert with id {id} not found")
    return response

@app.delete("/api/alerts/{id}")
async def remove_alert(id: str):
    response = await delete_alert(id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Alert with id {id} not found")
    return {"message": "Alert deleted successfully"}


# DONATIONS
@app.get("/api/donations")
async def get_donations():
    return await get_all_donations()

@app.get("/api/donations/{id}", response_model=DonationModel)
async def get_donation(id: str):
    donation = await get_donation_by_id(id)
    if not donation:
        raise HTTPException(status_code=404, detail=f"Donation with id {id} not found")
    return donation

@app.post("/api/donations", response_model=DonationModel)
async def save_donation(donation: DonationModel):
    response = await create_donation(donation.dict())
    if not response:
        raise HTTPException(status_code=400, detail="Error creating donation")
    return response

@app.put("/api/donations/{id}", response_model=DonationModel)
async def put_donation(id: str, donation: DonationModel):
    response = await update_donation(id, donation)
    if not response:
        raise HTTPException(status_code=404, detail=f"Donation with id {id} not found")
    return response

@app.delete("/api/donations/{id}")
async def remove_donation(id: str):
    response = await delete_donation(id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Donation with id {id} not found")
    return {"message": "Donation deleted successfully"}


# HOSPITALS
@app.get("/api/hospitals")
async def get_hospitals():
    return await get_all_hospitals()

@app.get("/api/hospitals/{id}", response_model=HospitalModel)
async def get_hospital(id: str):
    hospital = await get_hospital_by_id(id)
    if not hospital:
        raise HTTPException(status_code=404, detail=f"Hospital with id {id} not found")
    return hospital

@app.post("/api/hospitals", response_model=HospitalModel)
async def save_hospital(hospital: HospitalModel):
    response = await create_hospital(hospital.dict())
    if not response:
        raise HTTPException(status_code=400, detail="Error creating hospital")
    return response

@app.put("/api/hospitals/{id}", response_model=HospitalModel)
async def put_hospital(id: str, hospital: HospitalModel):
    response = await update_hospital(id, hospital)
    if not response:
        raise HTTPException(status_code=404, detail=f"Hospital with id {id} not found")
    return response

@app.delete("/api/hospitals/{id}")
async def remove_hospital(id: str):
    response = await delete_hospital(id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Hospital with id {id} not found")
    return {"message": "Hospital deleted successfully"}


# NOTIFICATIONS
@app.get("/api/notifications")
async def get_notifications():
    return await get_all_notifications()

@app.get("/api/notifications/{id}", response_model=NotificationModel)
async def get_notification(id: str):
    notification = await get_notification_by_id(id)
    if not notification:
        raise HTTPException(status_code=404, detail=f"Notification with id {id} not found")
    return notification

@app.post("/api/notifications", response_model=NotificationModel)
async def save_notification(notification: NotificationModel):
    response = await create_notification(notification.dict())
    if not response:
        raise HTTPException(status_code=400, detail="Error creating notification")
    return response

@app.put("/api/notifications/{id}", response_model=NotificationModel)
async def put_notification(id: str, notification: NotificationModel):
    response = await update_notification(id, notification)
    if not response:
        raise HTTPException(status_code=404, detail=f"Notification with id {id} not found")
    return response

@app.delete("/api/notifications/{id}")
async def remove_notification(id: str):
    response = await delete_notification(id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Notification with id {id} not found")
    return {"message": "Notification deleted successfully"}