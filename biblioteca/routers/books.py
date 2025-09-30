
import csv

from fastapi import APIRouter,HTTPException
from biblioteca.models import Book


router = APIRouter(prefix="/books", tags=["books"])


def get_author_by_id(author_id:str):
    with open('db/authors.csv',"r",newline="",encoding="utf-8") as csvfile:
        csv_dict_reader=csv.DictReader(csvfile)
        for author in csv_dict_reader:
            if author['id'] == author_id:
                return author
        raise HTTPException(status_code=404, detail="Author not found")

@router.get('')
def get_books():
    with open('db/books.csv',"r",newline="",encoding="utf-8") as csvfile:
        csv_dict_reader=csv.DictReader(csvfile)
        books=list(csv_dict_reader)
        for book in books:
            book.pop("id")
            author_id= book.pop("author_id")
            author = get_author_by_id(author_id)
            book["author_name"]=author["name"]
        return books

@router.get('/{book_title}')
def get_book(book_title:str):
    with open('db/books.csv',"r",newline="",encoding="utf-8") as csvfile:
        csv_dict_reader=csv.DictReader(csvfile)
        for book in csv_dict_reader:
            if book_title.lower() in book["title"].lower():
                book.pop("id")
                author_id= book.pop("author_id")
                author = get_author_by_id(author_id)
                book["author_name"]=author["name"]
                return book
        raise HTTPException(status_code=404, detail="Book not found")

@router.post('/create')
def create_book(book:Book):
    field_names=["id","title","author_id","available"]
    book_author =None
    with open('db/authors.csv',"r",newline="",encoding="utf-8") as csvfile:
        csv_dict_reader=csv.DictReader(csvfile)
        for author in csv_dict_reader:
            if author["id"]==book.author_id:
                book_author=author
    if book_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    with open('db/books.csv',"r+",newline="",encoding="utf-8") as csvfile:
        csvfile.seek(0)
        lines= len(csvfile.readlines())
        csv_dict_writer=csv.DictWriter(csvfile,fieldnames=field_names)
        csv_dict_writer.writerow({"id":lines,"title":book.title,"author_name":book.author_name,"available":True})
        return "Added book successfully"








