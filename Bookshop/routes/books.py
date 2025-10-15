

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from Bookshop.models import Book
from schemas import BookCreate, BookOut

router = APIRouter(prefix="/books", tags=["Books"])

# GET /books/{book_id} – obține o carte după ID
@router.get("/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# POST /books – creează o carte nouă
@router.post("/", response_model=BookOut)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    # Verificăm dacă titlul cărții deja există
    db_book = db.query(Book).filter(Book.title == book.title).first()
    if db_book:
        raise HTTPException(status_code=400, detail="Book with this title already exists")

    # Creăm obiectul
    new_book = Book(
        title=book.title,
        author_id=book.author_id,
        total_copies=book.total_copies,
        available_copies=book.total_copies
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book
