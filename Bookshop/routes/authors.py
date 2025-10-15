

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func  # doar dacă vrei verificare case-insensitive
from database import get_db
from models import Author
from schemas import AuthorCreate, AuthorOut

router = APIRouter(prefix="/authors", tags=["Authors"])

# GET /authors – lista tuturor autorilor
@router.get("/", response_model=list[AuthorOut])
def read_authors(db: Session = Depends(get_db)):
    return db.query(Author).all()

# POST /authors – crează un autor nou
@router.post("/", response_model=AuthorOut, status_code=status.HTTP_201_CREATED)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    # Verifică dacă autorul există deja (case-insensitive optional)
    existing = db.query(Author).filter(func.lower(Author.name) == author.name.lower()).first()
    if existing:
        raise HTTPException(status_code=400, detail="Author already exists")

    new_author = Author(name=author.name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

