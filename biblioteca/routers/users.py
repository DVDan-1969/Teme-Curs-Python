from fastapi import APIRouter
from fastapi import Request, HTTPException

router = APIRouter(prefix="/authors", tags=["authors"])



@router.post("/users/register")
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
        return {"message": "Autentificare reușită"}
    else:
        raise HTTPException(status_code=401, detail="Nume de utilizator sau parolă incorectă")

