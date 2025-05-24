from motor.motor_asyncio import AsyncIOMotorClient
from uuid import uuid4
from models import UserModel, UserUpdateModel, AppointmentModel, AlertModel, DonationModel, HospitalModel, NotificationModel
from bson import ObjectId
from fastapi import HTTPException

# URI de conexión
uri = "mongodb+srv://luisenriquelozanomejia:GogiverApp365@cluster0.tf6qc4g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Conectar cliente asíncrono
client = AsyncIOMotorClient(uri)

# Conectar a la base de datos
db = client["GoGiver_prototype"]

# Definir las colecciones como variables globales
users_collection = db["users"]
appointments_collection = db["appointments"]
alerts_collection = db["alerts"]
donations_collection = db["donations"]
hospitals_collection = db["hospitals"]
notifications_collection = db["notifications"]


# Funciones CRUD asíncronas para la colección users
async def get_all_users():
    cursor = users_collection.find({})
    users = []
    async for user in cursor:
        user["_id"] = str(user["_id"])  # Convertir ObjectId a string
        users.append(UserModel(**user))
    return users 

async def get_user_by_id(user_id):
    # Verificar si el ID es un ObjectId válido with httpexception
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    
    user = await users_collection.find_one({"_id": ObjectId(user_id)})
    return user

async def get_user_by_name(name: str):
    return await users_collection.find_one({"full_name": name})


async def create_user(user_data: dict):
    if "_id" not in user_data or user_data["_id"] is None:
        user_data["_id"] = ObjectId()  # Generar un ObjectId automáticamente
    result = await users_collection.insert_one(user_data)
    created_user = await users_collection.find_one({"_id": result.inserted_id})
    return created_user

async def update_user(user_id: str, update_data):
    user = {k: v for k, v in update_data.dict().items() if v is not None}
    print(user)
    await users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": user})
    result = await users_collection.find_one({"_id": ObjectId(user_id)})
    return result

async def delete_user(user_id: str):
    await users_collection.delete_one({"_id": ObjectId(user_id)})
    return True


# Funciones CRUD asíncronas para la colección appointments
async def get_all_appointments():
    cursor = appointments_collection.find({})
    appointments = []
    async for appointment in cursor:
        appointment["_id"] = str(appointment["_id"])  # Convertir ObjectId a string
        appointments.append(AppointmentModel(**appointment))
    return appointments 

async def get_appointment_by_id(appointment_id):
    # Verificar si el ID es un ObjectId válido with httpexception
    if not ObjectId.is_valid(appointment_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    
    appointment = await appointments_collection.find_one({"_id": ObjectId(appointment_id)})
    return appointment


async def create_appointment(appointment_data: dict):
    if "_id" not in appointment_data or appointment_data["_id"] is None:
        appointment_data["_id"] = ObjectId()  # Generar un ObjectId automáticamente
    result = await appointments_collection.insert_one(appointment_data)
    created_appointment = await appointments_collection.find_one({"_id": result.inserted_id})
    return created_appointment

async def update_appointment(appointment_id: str, update_data):
    appointment = {k: v for k, v in update_data.dict().items() if v is not None}
    print(appointment)
    await appointments_collection.update_one({"_id": ObjectId(appointment_id)}, {"$set": appointment})
    result = await appointments_collection.find_one({"_id": ObjectId(appointment_id)})
    return result

async def delete_appointment(appointment_id: str):
    await appointments_collection.delete_one({"_id": ObjectId(appointment_id)})
    return True

# Funciones CRUD asíncronas para la colección alerts

async def get_all_alerts():
    cursor = alerts_collection.find({})
    alerts = []
    async for alert in cursor:
        alert["_id"] = str(alert["_id"])  # Convertir ObjectId a string
        alerts.append(AlertModel(**alert))
    return alerts

async def get_alert_by_id(alert_id: str):
    if not ObjectId.is_valid(alert_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    alert = await alerts_collection.find_one({"_id": ObjectId(alert_id)})
    return alert

async def create_alert(alert_data: dict):
    if "_id" not in alert_data or alert_data["_id"] is None:
        alert_data["_id"] = ObjectId()
    result = await alerts_collection.insert_one(alert_data)
    created_alert = await alerts_collection.find_one({"_id": result.inserted_id})
    return created_alert

async def update_alert(alert_id: str, update_data):
    alert = {k: v for k, v in update_data.dict().items() if v is not None}
    await alerts_collection.update_one({"_id": ObjectId(alert_id)}, {"$set": alert})
    result = await alerts_collection.find_one({"_id": ObjectId(alert_id)})
    return result 

async def delete_alert(alert_id: str):
    await alerts_collection.delete_one({"_id": ObjectId(alert_id)})
    return True

# Funciones CRUD asíncronas para la colección donations

async def get_all_donations():
    cursor = donations_collection.find({})
    donations = []
    async for donation in cursor:
        donation["_id"] = str(donation["_id"])  # Convertir ObjectId a string
        donations.append(DonationModel(**donation))
    return donations

async def get_donation_by_id(donation_id: str):
    if not ObjectId.is_valid(donation_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    donation = await donations_collection.find_one({"_id": ObjectId(donation_id)})
    return donation

async def create_donation(donation_data: dict):
    if "_id" not in donation_data or donation_data["_id"] is None:
        donation_data["_id"] = ObjectId()
    result = await donations_collection.insert_one(donation_data)
    created_donation = await donations_collection.find_one({"_id": result.inserted_id})
    return created_donation

async def update_donation(donation_id: str, update_data):
    donation = {k: v for k, v in update_data.dict().items() if v is not None}
    await donations_collection.update_one({"_id": ObjectId(donation_id)}, {"$set": donation})
    result = await donations_collection.find_one({"_id": ObjectId(donation_id)})
    return result

async def delete_donation(donation_id: str):
    await donations_collection.delete_one({"_id": ObjectId(donation_id)})
    return True

# Funciones CRUD asíncronas para la colección hospitals

async def get_all_hospitals():
    cursor = hospitals_collection.find({})
    hospitals = []
    async for hospital in cursor:
        hospital["_id"] = str(hospital["_id"])
        hospitals.append(HospitalModel(**hospital))
    return hospitals

async def get_hospital_by_id(hospital_id: str):
    if not ObjectId.is_valid(hospital_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    hospital = await hospitals_collection.find_one({"_id": ObjectId(hospital_id)})
    return hospital

async def create_hospital(hospital_data: dict):
    if "_id" not in hospital_data or hospital_data["_id"] is None:
        hospital_data["_id"] = ObjectId()
    result = await hospitals_collection.insert_one(hospital_data)
    created_hospital = await hospitals_collection.find_one({"_id": result.inserted_id})
    return created_hospital

async def update_hospital(hospital_id: str, update_data):
    hospital = {k: v for k, v in update_data.dict().items() if v is not None}
    await hospitals_collection.update_one({"_id": ObjectId(hospital_id)}, {"$set": hospital})
    result = await hospitals_collection.find_one({"_id": ObjectId(hospital_id)})
    return result

async def delete_hospital(hospital_id: str):
    await hospitals_collection.delete_one({"_id": ObjectId(hospital_id)})
    return True

# Funciones CRUD asíncronas para la colección notifications

async def get_all_notifications():
    cursor = notifications_collection.find({})
    notifications = []
    async for notification in cursor:
        notification["_id"] = str(notification["_id"])
        notifications.append(NotificationModel(**notification))
    return notifications

async def get_notification_by_id(notification_id: str):
    if not ObjectId.is_valid(notification_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    notification = await notifications_collection.find_one({"_id": ObjectId(notification_id)})
    return notification

async def create_notification(notification_data: dict):
    if "_id" not in notification_data or notification_data["_id"] is None:
        notification_data["_id"] = ObjectId()
    result = await notifications_collection.insert_one(notification_data)
    created_notification = await notifications_collection.find_one({"_id": result.inserted_id})
    return created_notification

async def update_notification(notification_id: str, update_data):
    notification = {k: v for k, v in update_data.dict().items() if v is not None}
    await notifications_collection.update_one({"_id": ObjectId(notification_id)}, {"$set": notification})
    result = await notifications_collection.find_one({"_id": ObjectId(notification_id)})
    return result

async def delete_notification(notification_id: str):
    await notifications_collection.delete_one({"_id": ObjectId(notification_id)})
    return True




try:
    client.admin.command('ping')
    print("✅ Conectado a MongoDB correctamente")
except Exception as e:
    print("❌ Error de conexión:", e)



if __name__ == "__main__":
    print("📦 Estado de la base de datos:")
    
    # Mostrar el nombre de la base de datos actual
    print(f"Base de datos conectada: {db.name}")
    
    # Listar todas las colecciones disponibles (incluyendo las manualmente creadas)
    print("📂 Colecciones disponibles en la base de datos:")
    for collection_name in db.list_collection_names():
        print(f" - {collection_name}")

    print("\n📋 Usuarios en la base de datos:")
    for user in users_collection.find():
        print(user)