from fastapi import APIRouter, HTTPException
from fastapi import FastAPI
from models import UserModel, UserUpdateModel
from database import (
    get_all_users, get_user_by_id, create_user, update_user, delete_user, get_user_by_name
)
user_router = APIRouter()

@user_router.get("/api/users")
async def get_users():
    users = await get_all_users() 
    return users


@user_router.post("/api/users", response_model=UserModel)
async def save_user(user: UserModel):
    userFound =await get_user_by_name(user.full_name)
    if userFound:
        raise HTTPException(status_code=400, detail="User already exists")
    
    response = await create_user(user.dict())
    if not response:
        raise HTTPException(status_code=400, detail="Error creating user")
    return response

@user_router.get("/api/users/{id}", response_model=UserModel)
async def get_user(id: str):
    user = await get_user_by_id(id)
    if not user: 
        raise HTTPException(status_code=404, detail="User with id {id} not found")
    return user


@user_router.put("/api/users/{id}", response_model=UserModel)
async def put_user(id: str, user: UserUpdateModel):
    response = await update_user(id, user)
    if not response:
        raise HTTPException(status_code=404, detail="User with id {id} not found")
    return response


@user_router.delete("/api/users/{id}")
async def remove_user(id: str): 
    response = await delete_user(id)
    if not response:
        raise HTTPException(status_code=404, detail="User with id {id} not found") 
    return {"message": "User deleted successfully"}
