from pydantic import BaseModel
from typing import List, Optional
from decimal import Decimal

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    posts: List['Post'] = []
    class Config:
        from_attributes = True

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int
    class Config:
        from_attributes = True

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    login: Optional[str] = None
    password: Optional[str] = None

class LoginRequest(BaseModel):
    login: str
    password: str

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    login: str
    password: str

class EmployeeResponse(BaseModel):
    employee_id: int
    first_name: str
    last_name: str
    login: str
    status_id: int
    class Config:
        from_attributes = True

class ProductResponse(BaseModel):
    product_id: int
    product_name: str
    price: Decimal
    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    order_id: int
    client_id: int
    employee_id: int
    order_date: str
    total_amount: Decimal
    status_id: int
    class Config:
        from_attributes = True

