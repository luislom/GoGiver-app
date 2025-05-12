from motor.motor_asyncio import AsyncIOMotorClient
from uuid import uuid4
from models import UserModel
# URI de conexión
uri = "mongodb+srv://luisenriquelozanomejia:GogiverApp365@cluster0.tf6qc4g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Conectar cliente asíncrono
client = AsyncIOMotorClient(uri)

# Conectar a la base de datos
db = client["GoGiver_prototype"]  # Puedes usar otro nombre si quieres

# Definir las colecciones como variables globales
users_collection = db["users"]
appointments_collection = db["appointments"]
alerts_collection = db["alerts"]
donations_collection = db["donations"]
hospitals_collection = db["hospitals"]
notifications_collection = db["notifications"]

from bson import ObjectId

# Funciones CRUD asíncronas para la colección users
async def get_all_users():
    cursor = users_collection.find({})
    users = []
    async for user in cursor:
        user["_id"] = str(user["_id"])  # Convertir ObjectId a string
        users.append(UserModel(**user))
    return users 

async def get_user_by_id(user_id: str):
    return await users_collection.find_one({"_id": ObjectId(user_id)})

async def get_user_by_name(name: str):
    return await users_collection.find_one({"full_name": name})


async def create_user(user_data: dict):
    if "_id" not in user_data or user_data["_id"] is None:
        user_data["_id"] = ObjectId()  # Generar un ObjectId automáticamente
    result = await users_collection.insert_one(user_data)
    created_user = await users_collection.find_one({"_id": result.inserted_id})
    return created_user

async def update_user(user_id: str, update_data: dict):
    await users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    result = await users_collection.find_one({"_id": ObjectId(user_id)})
    return result.modified_count

async def delete_user(user_id: str):
    await users_collection.delete_one({"_id": ObjectId(user_id)})
    return True




# # Funciones CRUD asíncronas para la colección appointments

# async def get_all_appointments():
#     cursor = appointments_collection.find({})
#     items = []
#     async for item in cursor:
#         items.append(item)
#     return items

# async def create_appointment(data: dict):
#     result = await appointments_collection.insert_one(data)
#     return str(result.inserted_id)

# async def update_appointment(appointment_id: str, update_data: dict):
#     result = await appointments_collection.update_one({"_id": ObjectId(appointment_id)}, {"$set": update_data})
#     return result.modified_count

# async def delete_appointment(appointment_id: str):
#     result = await appointments_collection.delete_one({"_id": ObjectId(appointment_id)})
#     return result.deleted_count

# async def get_all_alerts():
#     cursor = alerts_collection.find({})
#     items = []
#     async for item in cursor:
#         items.append(item)
#     return items

# async def create_alert(data: dict):
#     result = await alerts_collection.insert_one(data)
#     return str(result.inserted_id)

# async def update_alert(alert_id: str, update_data: dict):
#     result = await alerts_collection.update_one({"_id": ObjectId(alert_id)}, {"$set": update_data})
#     return result.modified_count

# async def delete_alert(alert_id: str):
#     result = await alerts_collection.delete_one({"_id": ObjectId(alert_id)})
#     return result.deleted_count

# async def get_all_donations():
#     cursor = donations_collection.find({})
#     items = []
#     async for item in cursor:
#         items.append(item)
#     return items

# async def create_donation(data: dict):
#     result = await donations_collection.insert_one(data)
#     return str(result.inserted_id)

# async def update_donation(donation_id: str, update_data: dict):
#     result = await donations_collection.update_one({"_id": ObjectId(donation_id)}, {"$set": update_data})
#     return result.modified_count

# async def delete_donation(donation_id: str):
#     result = await donations_collection.delete_one({"_id": ObjectId(donation_id)})
#     return result.deleted_count

# async def get_all_hospitals():
#     cursor = hospitals_collection.find({})
#     items = []
#     async for item in cursor:
#         items.append(item)
#     return items

# async def create_hospital(data: dict):
#     result = await hospitals_collection.insert_one(data)
#     return str(result.inserted_id)

# async def update_hospital(hospital_id: str, update_data: dict):
#     result = await hospitals_collection.update_one({"_id": ObjectId(hospital_id)}, {"$set": update_data})
#     return result.modified_count

# async def delete_hospital(hospital_id: str):
#     result = await hospitals_collection.delete_one({"_id": ObjectId(hospital_id)})
#     return result.deleted_count

# async def get_all_notifications():
#     cursor = notifications_collection.find({})
#     items = []
#     async for item in cursor:
#         items.append(item)
#     return items

# async def create_notification(data: dict):
#     result = await notifications_collection.insert_one(data)
#     return str(result.inserted_id)

# async def update_notification(notification_id: str, update_data: dict):
#     result = await notifications_collection.update_one({"_id": ObjectId(notification_id)}, {"$set": update_data})
#     return result.modified_count

# async def delete_notification(notification_id: str):
#     result = await notifications_collection.delete_one({"_id": ObjectId(notification_id)})
#     return result.deleted_count

# Confirmar conexión
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