from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="posts")

class Employee(Base):
    __tablename__ = "employee"
    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    login = Column(String, unique=True)
    password = Column(String)
    status_id = Column(Integer)

class Product(Base):
    __tablename__ = "product"
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    price = Column(DECIMAL(10, 2))

class Orderr(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True)
    client_id = Column(Integer)
    employee_id = Column(Integer)
    order_date = Column(DateTime, default=func.now())
    total_amount = Column(DECIMAL(10, 2))
    status_id = Column(Integer)
