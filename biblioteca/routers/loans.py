
import csv

from fastapi import APIRouter,HTTPException

from models import Loans
from collections import Counter
router = APIRouter(prefix="/loans", tags=["loans"])


router.get("")
def get_loans():
    with open('db/loans.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        loans = []
        for row in csv_dict_reader:
            loan = {
                "username": row["username"],
                "book_id": row["book_id"],
                "returned": row["returned"]
            }
            loans.append(loan)
        return loans


@router.get('/user/{username}')
def get_loans_by_username(username: str):
    with open('db/loans.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        user_loans = []
        for row in csv_dict_reader:
            if row["username"].lower() == username.lower():
                loan = {
                    "book_id": row["book_id"],
                    "returned": row["returned"]
                }
                user_loans.append(loan)

        if not user_loans:
            raise HTTPException(status_code=404, detail="No loans found for this user")

        return {
            "username": username,
            "loans": user_loans
        }
@router.post('/create')
def create_return(loan:Loans):
    field_names = ["id", "username","book_id","returned"]
    with open('db/loans.csv', "r+", newline="", encoding="utf-8") as csvfile:
        csvfile.seek(0)
        lines = len(csvfile.readlines())
        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=field_names)
        csv_dict_writer.writerow({"id": lines, "username":loan.username, "book_id":loan.book_id, "returned":loan.returned})
        return "Added return/ successfully"


def cele_mai_imprumutate_carti():
    # Încarcă titlurile cărților într-un dicționar
    carti = {}
    with open('db/books.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            carti[row['id']] = row['title']

    # Numără împrumuturile după book_id
    counter = Counter()
    with open('db/loans.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            book_id = row['book_id']
            counter[book_id] += 1

    # Obține cele mai comune 5 cărți
    cele_mai_imprumutate = counter.most_common(5)

    # Formatează rezultatele cu titlurile
    rezultate = []
    for book_id, count in cele_mai_imprumutate:
        titlu = carti.get(book_id, 'Titlu necunoscut')
        rezultate.append((titlu, count))

    return rezultate

@router.get("/top-carti")
def get_top_carti():
    return cele_mai_imprumutate_carti()






