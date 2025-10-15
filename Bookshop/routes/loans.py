

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from Bookshop.models import Loans, Book
from schemas import LoanCreate, LoanOut

router = APIRouter(prefix="/loans", tags=["Loans"])


# GET /loans – toate împrumuturile
@router.get("/", response_model=list[LoanOut])
def get_loans(db: Session = Depends(get_db)):
    return db.query(Loans).all()


# POST /loans – creează un împrumut
@router.post("/", response_model=LoanOut, status_code=status.HTTP_201_CREATED)
def create_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    # Verifică dacă există cartea
    book = db.query(Book).filter(Book.id == loan.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Creează împrumutul
    new_loan = Loans(book_id=loan.book_id)
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)

    return new_loan


# Funcție auxiliară: top 5 cele mai împrumutate cărți
def cele_mai_imprumutate_carti(db: Session):
    rezultate = (
        db.query(Book.title, func.count(Loans.id).label("nr_imprumuturi"))
        .join(Loans, Book.id == Loans.book_id)
        .group_by(Book.id)
        .order_by(func.count(Loans.id).desc())
        .limit(5)
        .all()
    )
    return [{"titlu": r[0], "numar_imprumuturi": r[1]} for r in rezultate]


# GET /loans/top-carti – top 5 cele mai împrumutate cărți
@router.get("/top-carti")
def get_top_carti(db: Session = Depends(get_db)):
    return cele_mai_imprumutate_carti(db)

