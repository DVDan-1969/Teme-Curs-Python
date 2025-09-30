
import csv

from fastapi import APIRouter,HTTPException
# from biblioteca.models import Author
from biblioteca.models import Author

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get('')
def get_authors():
    with open('db/authors.csv',"r",newline="",encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        authors=list(csv_dict_reader)
        for author in authors:
            author.pop("id")
        return authors

@router.get('/get_author')
def get_author(author_name:str):
    with open('db/authors.csv',"r",newline="",encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        for author in csv_dict_reader:
            if author_name.lower() in author["name"].lower():
                author.pop("id")
                return author
        raise HTTPException(status_code=404, detail="Author not found")

@router.post('/create')
def create_author(author:Author):
    field_names=["id","name"]
    with open('db/authors.csv',"r+",newline="",encoding="utf-8") as csvfile:
        csvfile.seek(0)
        lines = len(csvfile.readlines())
        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=field_names)
        csv_dict_writer.writerow({"id":lines,"name":author.name})
        return "Added author successfully"




