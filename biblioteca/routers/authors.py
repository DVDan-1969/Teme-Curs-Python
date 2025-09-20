from fastapi import APIRouter
from models import Author

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("")
def list_authors():
    return get_authors()

@router.post("/add")
def add_new_author(author: Author):
    add_author(author)
    return {"message": "Autor adăugat cu succes"}

@router.get("/search")
def search_authors(name: str):
    results = search_author_by_name(name)
    return results
