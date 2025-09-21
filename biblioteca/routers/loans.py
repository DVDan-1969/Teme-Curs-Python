
# from fastapi import APIRouter
# from fastapi import Request, HTTPException
#
# router = APIRouter(prefix="/authors", tags=["authors"])
# router = APIRouter(prefix="/loans", tags=["loans"])
#
#
#
# @router.post("/loans/{id}")
# @router.post("/{id}")
# def borrow_book(id: str, request: Request):
#     data = request.json()
#     username = data.get('username')

from fastapi import APIRouter, Request, HTTPException
from models import Loan
from fastapi import status

router = APIRouter(prefix="/loans", tags=["loans"])

@router.post("/{id}")
async def borrow_book(id: str, loan: Loan):
    # Încearcă să găsești utilizatorul și cartea
    books = get_books()
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cartea nu a fost găsită")

    users = get_users()
    user = next((u for u in users if u['username'] == loan.user), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilizatorul nu a fost găsit")

    # Verifică dacă cartea este disponibilă
    if book['available'] == 'False':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cartea nu este disponibilă pentru împrumut")

    # Adăugarea împrumutului
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
