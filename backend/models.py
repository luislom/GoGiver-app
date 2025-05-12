from uuid import uuid4
from pydantic import BaseModel, Field
from bson import ObjectId

from typing import Literal, Optional
from fastapi import HTTPException
from datetime import date

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
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    # role: Literal["donante", "receptor", "admin"]
    # blood_type: Literal["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
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














