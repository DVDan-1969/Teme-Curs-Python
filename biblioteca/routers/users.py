from fastapi import APIRouter
from fastapi import HTTPException
from models import User

from helper import add_user, authenticate_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
def register_user(user: User):
    add_user(user)
    return {"message": "Utilizator înregistrat cu succes"}

@router.post("/login")
def login_user(user: User):
    if authenticate_user(user.username, user.password):
        return {"message": "Autentificare reușită"}
    else:
        raise HTTPException(status_code=401, detail="Nume de utilizator sau parolă incorectă")

