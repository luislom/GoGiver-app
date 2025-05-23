from uuid import uuid4
from pydantic import BaseModel, Field
from bson import ObjectId

from typing import Literal, Optional, Any
from fastapi import HTTPException
from datetime import date
from datetime import datetime

from bson import ObjectId
from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema
from typing import Any

class PyObjectId(str):
    @classmethod
    def __get_pydantic_core_schema__(
            cls, _source_type: Any, _handler: Any
    ) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema([
                core_schema.is_instance_schema(ObjectId),
                core_schema.chain_schema([
                    core_schema.str_schema(),
                    core_schema.no_info_plain_validator_function(cls.validate),
                ])
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: str(x)
            ),
        )

    @classmethod
    def validate(cls, value) -> ObjectId:
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return ObjectId(value)




# Modelo de Usuario
class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=ObjectId, alias="_id")  # Hacer que el campo sea opcional
    full_name: str 
    email: Optional[str] = None
    phone: Optional[str] = None
    blood_type: Optional[Literal["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]] = None
    birth_date: Optional[date] = None
    location: Optional[str] = None
    last_donation: Optional[date] = None
    available_to_donate: bool = True

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }

# Modelo de Usuario para actualizar
class UserUpdateModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=ObjectId, alias="_id")
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    blood_type: Optional[Literal["A+", "A-", "B+", "B-", "AB+", "AB-", "O+"]] = None
    birth_date: Optional[date] = None
    location: Optional[str] = None
    last_donation: Optional[date] = None
    available_to_donate: bool = True

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }

# Modelos para otras colecciones


class AppointmentModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=ObjectId, alias="_id")
    user_id: str 
    hospital_id: str
    scheduled_at: datetime 
    confirmed: Optional[bool] = False
    attended: Optional[bool] = False

    model_config = {
        "populate_by_name": True,
        "from_attributes": True,
        "json_encoders": {ObjectId: str}
    }

class AppointmentUpdateModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=ObjectId, alias="_id")
    user_id: Optional[str] = None
    hospital_id: Optional[str] = None
    scheduled_at: Optional[datetime] = None
    confirmed: Optional[bool] = None
    attended: Optional[bool] = None

    model_config = {
        "populate_by_name": True,
        "from_attributes": True,
        "json_encoders": {ObjectId: str}
    }



class AlertModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=ObjectId, alias="_id")
    blood_type: Optional[Literal["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]] = None
    city: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    hospital_id: Optional[str] = None
    status: Optional[Literal["activa", "resuelta", "cancelada"]] = "activa"

    model_config = {
        "populate_by_name": True,
        "from_attributes": True,
        "json_encoders": {ObjectId: str}
    }

class DonationModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=ObjectId, alias="_id")
    user_id: Optional[str] = None
    date: Optional[datetime] = None
    hospital_id: Optional[str] = None
    volume_ml: Optional[int] = 450

    model_config = {
        "populate_by_name": True,
        "from_attributes": True,
        "json_encoders": {ObjectId: str}
    }

class HospitalModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=ObjectId, alias="_id")
    name: str = None
    city: str = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

    model_config = {
        "populate_by_name": True,
        "from_attributes": True,
        "json_encoders": {ObjectId: str}
    }

class NotificationModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=ObjectId, alias="_id")
    user_id: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    read: Optional[bool] = False

    model_config = {
        "populate_by_name": True,
        "from_attributes": True,
        "json_encoders": {ObjectId: str}
    }



















