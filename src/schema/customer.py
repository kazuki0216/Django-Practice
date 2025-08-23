from pydantic import BaseModel
from datetime import datetime


class CustomerCreateRequest(BaseModel):
    name: str
    email: str
    phone_number: str


class CustomerCreateResponse(BaseModel):
    name: str
    email: str
    phone_number: str
    created_at: datetime


class CustomerGetRequest(BaseModel):
    name: str
    email: str


class CustomerGetResponse(BaseModel):
    name: str
    email: str
    phone_number: str
    created_at: datetime
