from fastapi import  APIRouter
router = APIRouter(prefix="/authors", tags=["authors"])



@router.get("/books")
def list_books():
    return get_books()

@router.post("/books/add")
def add_new_book(book: Book):
    add_book(book)
    return {"message": "Carte adăugată cu succes"}

@router.get("/books/search")
def search_books(title: str):
    results = search_books_by_title(title)
    return results
@router.get("/stats/top-books")
def top_books():
    top = get_top_books()
    return top
