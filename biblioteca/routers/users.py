
from fastapi import APIRouter
from fastapi import Request,
from fastapi import HTTPException
from models import User

router = APIRouter(prefix="/authors", tags=["authors"])
from helper import add_user, authenticate_user

router = APIRouter(prefix="/users", tags=["users"])





@router.post("/users/register")
@router.post("/register")
def register_user(user: User):
    add_user(user)
    return {"message": "Utilizator înregistrat cu succes"}

@router.post("/users/login")
def login_user(request: Request):
    data = request.json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        raise HTTPException(status_code=400, detail="Numele de utilizator și parola sunt obligatorii")
    if authenticate_user(username, password):
@router.post("/login")
def login_user(user: User):
    if authenticate_user(user.username, user.password):
        return {"message": "Autentificare reușită"}
    else:
        raise HTTPException(status_code=401, detail="Nume de utilizator sau parolă incorectă")



