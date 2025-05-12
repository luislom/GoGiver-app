from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
from database import get_all_users, create_user, get_user_by_name, get_user_by_id, update_user, delete_user
from models import UserModel
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

@app.get("/api/users/{id}")
async def get_user_by_id():
    return "single user"


@app.put("/api/users/{id}")
async def update_user():
    return "updating user"


@app.delete("/api/users/{id}")
async def delete_users():
    return "delete user"
