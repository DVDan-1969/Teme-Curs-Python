
import csv

from fastapi import APIRouter,HTTPException

from models import Loans

router = APIRouter(prefix="/loans", tags=["loans"])


@router.get('')
def get_loans():
    with open('db/books.csv',"r",newline="",encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        loans=list(csv_dict_reader)
        for loan in loans:
            loan.pop("id")
        return loans

@router.get('/get_loan')
def get_loan(user:str):
        with open('db/authors.csv',"r",newline="",encoding="utf-8") as csvfile:
            csv_dict_reader = csv.DictReader(csvfile)
        for loan in csv_dict_reader:
            if user.lower() in loan["user"].lower():
                loan.pop("id")
                return loan
        raise HTTPException(status_code=404, detail="Loan not found")


@router.post('/create')
def create_return(loan:Loans):
    field_names = ["id", "user","book_id","returned"]
    with open('db/authors.csv', "r+", newline="", encoding="utf-8") as csvfile:
        csvfile.seek(0)
        lines = len(csvfile.readlines())
        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=field_names)
        csv_dict_writer.writerow({"id": lines, "user":loan.user, "book_id":loan.book_id, "returned":loan.returned})
        return "Added return/ successfully"






