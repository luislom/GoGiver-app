from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware



from routes.user import user_router
from routes.appointments import appointment_router
from routes.alerts import alert_router
from routes.donations import donation_router
from routes.hospitals import hospital_router
from routes.notifications import notification_router



app = FastAPI()



@app.get("/")

def welcome():
    return {"message":"Welcome to GoGiver App"}


app.include_router(user_router)
app.include_router(appointment_router)
app.include_router(alert_router)
app.include_router(donation_router)
app.include_router(hospital_router)
app.include_router(notification_router)