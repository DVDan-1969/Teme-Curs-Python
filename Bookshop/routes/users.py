

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Bookshop.models import User
from schemas import UserCreate, UserLogin, UserOut
from database import SessionLocal
from database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

# GET /users – lista tuturor utilizatorilor
@router.get("/", response_model=list[UserOut])
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


# POST /users – crearea unui utilizator
@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    new_user = User(
        username=user.username,
        password=user.password,  # vezi mai jos recomandarea legată de hashing
        email=user.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# POST /users/login – autentificare utilizator
@router.post("/login")
def login_user(login_data: UserLogin, db: Session = Depends(get_db)):
    # Caută utilizatorul după username
    db_user = db.query(User).filter(User.username == login_data.username).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Username not found")

    if db_user.password != login_data.password:
        raise HTTPException(status_code=400, detail="Incorrect password")

    return {"message": "Login successful"}

