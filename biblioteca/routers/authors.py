



from fastapi import APIRouter
from typing import List
from models import Author

router = APIRouter(prefix="/authors", tags=["authors"])

@router.get("", response_model=List[Author])
def list_authors():
    return get_authors()

@router.post("", response_model=Author)
def add_new_author(author: Author):
    add_author(author)
    return author

@router.get("/search", response_model=List[Author])
def search_authors(name: str):
    results = search_author_by_name(name)
    return results
