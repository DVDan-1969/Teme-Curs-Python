
# from fastapi import APIRouter
# from fastapi import Request, HTTPException
# from fastapi import HTTPException
# from models import User
#
# router = APIRouter(prefix="/authors", tags=["authors"])
# from helper import add_user, authenticate_user
#
# router = APIRouter(prefix="/users", tags=["users"])
#
#
# @router.post("/users/register")
# @router.post("/register")
# def register_user(user: User):
#     add_user(user)
#     return {"message": "Utilizator înregistrat cu succes"}
#
# @router.post("/users/login")
# def login_user(request: Request):
#     data = request.json()
#     username = data.get('username')
#     password = data.get('password')
#     if not username or not password:
#         raise HTTPException(status_code=400, detail="Numele de utilizator și parola sunt obligatorii")
#     if authenticate_user(username, password):
# @router.post("/login")
# def login_user(user: User):
#     if authenticate_user(user.username, user.password):
#         return {"message": "Autentificare reușită"}
#     else:
#         raise HTTPException(status_code=401, detail="Nume de utilizator sau parolă incorectă")

from fastapi import APIRouter, HTTPException, status
from models import Loan
from typing import List

router = APIRouter(prefix="/loans", tags=["loans"])

@router.post("/{id}")
async def borrow_book(id: str, loan: Loan):
    # Verifică dacă există cartea
    books = get_books()
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cartea nu a fost găsită")

    # Verifică dacă există utilizatorul
    users = get_users()
    user = next((u for u in users if u['username'] == loan.user), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilizatorul nu a fost găsit")

    # Verifică dacă cartea este disponibilă
    if book['available'] == 'False':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cartea nu este disponibilă pentru împrumut")

    # Crează un împrumut
    loan_data = {
        "id": id,
        "user": loan.user,
        "book_id": id,
        "returned": False
    }
    add_loan(loan_data)

    # Actualizează disponibilitatea cărții
    book['available'] = 'False'
    write_csv('db/books.csv', books, ['id', 'title', 'author_id', 'available'])

    return {"message": f"Cartea '{book['title']}' a fost împrumutată de {loan.user} cu succes"}