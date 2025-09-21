
# from fastapi import  APIRouter
# router = APIRouter(prefix="/authors", tags=["authors"])
# from models import Book
#
# router = APIRouter(prefix="/books", tags=["books"])
#
#
# @router.get("/books")
#
# @router.get("")
# def list_books():
#     return get_books()
#
# @router.post("/books/add")
# @router.post("/add")
# def add_new_book(book: Book):
#     add_book(book)
#     return {"message": "Carte adăugată cu succes"}
#
# @router.get("/books/search")
# @router.get("/search")
# def search_books(title: str):
#     results = search_books_by_title(title)
#     return results
#
# @router.get("/stats/top-books")
# def top_books():
#     top = get_top_books()

from fastapi import APIRouter
from typing import List
from models import Book

router = APIRouter(prefix="/books", tags=["books"])

@router.get("", response_model=List[Book])
def list_books():
    return get_books()

@router.post("", response_model=Book)
def add_new_book(book: Book):
    add_book(book)
    return book

@router.get("/search", response_model=List[Book])
def search_books(title: str):
    results = search_books_by_title(title)
    return results

@router.get("/stats/top-books", response_model=List[Book])
def top_books():
    top = get_top_books()
    return top