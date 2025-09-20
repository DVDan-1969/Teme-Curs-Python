import csv
import os
from typing import List
from uuid import uuid4

from fastapi import HTTPException


def read_csv(file_path: str):
    data = []
    if not os.path.exists(file_path):  # verificare existenta fisier
        return data
    try:
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"Erroare la citirea fișierului {file_path}: {e}")
    return data


def write_csv(file_path: str, data: List[dict], fieldnames: List[str]):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Erroare la scrierea în fișierul {file_path}: {e}")


USERS_FILE = 'db/users.csv'


def get_users():
    return read_csv(USERS_FILE)


def add_user(user):
    users = get_users()
    # Verificare duplicat
    if any(u['username'] == user.username for u in users):
        raise HTTPException(status_code=400, detail="Utilizator deja existent")
    users.append(user.dict())
    write_csv(USERS_FILE, users, ['username', 'password'])


def authenticate_user(username: str, password: str):
    users = get_users()
    for u in users:
        if u['username'] == username and u['password'] == password:
            return True
    return False


AUTHORS_FILE = 'db/authors.csv'


def get_authors():
    return read_csv(AUTHORS_FILE)


def add_author(author):
    authors = get_authors()
    if any(a['name'] == author.name for a in authors):
        raise HTTPException(status_code=400, detail="Autor deja existent")
    authors.append(author.dict())
    write_csv(AUTHORS_FILE, authors, ['id', 'name'])


def search_author_by_name(name: str):
    authors = get_authors()
    return [a for a in authors if name.lower() in a['name'].lower()]


BOOKS_FILE = 'db/books.csv'


def get_books():
    return read_csv(BOOKS_FILE)


def add_book(book):
    books = get_books()
    if any(b['title'] == book.title for b in books):
        raise HTTPException(status_code=400, detail="Cartea deja există")
    books.append(book.dict())
    write_csv(BOOKS_FILE, books, ['id', 'title', 'author_id', 'available'])


def search_books_by_title(title: str):
    books = get_books()
    return [b for b in books if title.lower() in b['title'].lower()]


LOANS_FILE = 'db/loans.csv'


def get_loans():
    return read_csv(LOANS_FILE)


# verificare carte imprumutata
def add_loan(user: str, book_id: str):
    books = get_books()
    book = next((b for b in books if b['id'] == book_id), None)
    # functia next returneaza primul element care indeplineste conditia
    if not book:
        raise HTTPException(status_code=404, detail="Cartea nu a fost găsită")
    if book['available'] == 'False':
        raise HTTPException(status_code=400, detail="Cartea nu este disponibilă")
    # Marcare carte ca indisponibilă
    book['available'] = 'False'
    # Salvare cărți modificate
    write_csv(BOOKS_FILE, books, ['id', 'title', 'author_id', 'available'])

    # Creare împrumut
    loans = get_loans()
    loan_id = str(uuid4())
    loan = {
        'id': loan_id,
        'user': user,
        'book_id': book_id,
        'returned': 'False'
    }
    loans.append(loan)
    write_csv(LOANS_FILE, loans, ['id', 'user', 'book_id', 'returned'])
    return loan


def get_top_books():
    loans = get_loans()
    books = get_books()
    # Calcularea celor mai împrumutate cărți
    count_dict = {}
    for loan in loans:
        if loan['returned'] == 'False':
            continue
        book_id = loan['book_id']
        count_dict[book_id] = count_dict.get(book_id, 0) + 1
    # Sortare după frecvență
    sorted_books = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    top5_ids = [b[0] for b in sorted_books[:5]]
    top_books = [b for b in books if b['id'] in top5_ids]
    return top_books
