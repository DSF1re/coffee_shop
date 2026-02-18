from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from database import engine, Base, get_db
import models
import schemas
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Coffee Like API",
    description="API для управления кофейней",
    version="1.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене замени на конкретный адрес, например ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FastAPI Coffee Like запущен!"}

@app.post("/api/user/login")
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    emp = crud.auth_employee(db, request)
    if not emp:
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")
    return {
        "userId": emp.employee_id,
        "userName": emp.first_name,
        "login": emp.login
    }

@app.post("/api/user/register", status_code=201)
def register(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    try:
        crud.create_employee(db, emp)
        return {"message": "Сотрудник успешно зарегистрирован"}
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Ошибка регистрации: {str(ex)}")

@app.get("/api/user", response_model=List[schemas.EmployeeResponse])
def read_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.get("/api/user/{id}", response_model=schemas.EmployeeResponse)
def read_employee(id: int, db: Session = Depends(get_db)):
    emp = crud.get_employee(db, id)
    if not emp:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")
    return emp
    
@app.put("/api/user/{id}", response_model=schemas.EmployeeResponse)
def update_employee_profile(id: int, emp: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_emp = crud.update_employee(db, id, emp)
    if not db_emp:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")
    return db_emp

@app.delete("/api/user/{id}")
def remove_employee(id: int, db: Session = Depends(get_db)):
    emp = crud.delete_employee(db, id)
    if not emp:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")
    return {"message": "Удалено"}

@app.get("/api/product", response_model=List[schemas.ProductResponse])
def read_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@app.get("/api/product/{id}", response_model=schemas.ProductResponse)
def read_product(id: int, db: Session = Depends(get_db)):
    prod = crud.get_product(db, id)
    if not prod:
        raise HTTPException(status_code=404, detail="Товар отсутствует")
    return prod

@app.get("/api/orders/{id}", response_model=schemas.OrderResponse)
def read_order(id: int, db: Session = Depends(get_db)):
    order = crud.get_order(db, id)
    if not order:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return order

@app.post("/api/orders", status_code=201)
def create_order(
    client_id: int, 
    employee_id: int, 
    total_amount: float, 
    status_id: int, 
    db: Session = Depends(get_db)
):
    db_order = models.Orderr(
        client_id=client_id,
        employee_id=employee_id,
        total_amount=total_amount,
        status_id=status_id
    )
    try:
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return {"message": "Заказ создан", "order_id": db_order.order_id}
    except Exception as ex:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Ошибка создания заказа: {str(ex)}")