from fastapi import APIRouter
from fastapi import Request, HTTPException

router = APIRouter(prefix="/loans", tags=["loans"])



@router.post("/{id}")
def borrow_book(id: str, request: Request):
    data = request.json()
    username = data.get('username')
    password = data.get('password')
    if not authenticate_user(username, password):
        raise HTTPException(status_code=401, detail="Autentificare eșuată")
    loan = add_loan(username, id)
    return {"message": "Cartea a fost împrumutată", "loan": loan}


