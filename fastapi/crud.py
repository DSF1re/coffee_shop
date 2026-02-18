from sqlalchemy.orm import Session
from models import User, Post, Employee, Product, Orderr
from schemas import UserCreate, PostCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_post_for_user(db: Session, post: PostCreate, user_id: int):
    db_post = Post(**post.dict(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def auth_employee(db: Session, login_request: LoginRequest):
    return db.query(Employee).filter(
        Employee.login == login_request.login,
        Employee.password == login_request.password
    ).first()

def create_employee(db: Session, emp: EmployeeCreate):
    db_emp = Employee(**emp.dict(), status_id=1)
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

def update_employee(db: Session, employee_id: int, emp_data: EmployeeUpdate):
    db_emp = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if db_emp:
        update_data = emp_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_emp, key, value)
        
        db.commit()
        db.refresh(db_emp)
    return db_emp

def get_employees(db: Session):
    return db.query(Employee).all()

def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.employee_id == employee_id).first()

def delete_employee(db: Session, employee_id: int):
    emp = get_employee(db, employee_id)
    if emp:
        db.delete(emp)
        db.commit()
    return emp

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.product_id == product_id).first()

def get_products(db: Session):
    return db.query(Product).all()

def get_order(db: Session, order_id: int):
    return db.query(Orderr).filter(Orderr.order_id == order_id).first()
