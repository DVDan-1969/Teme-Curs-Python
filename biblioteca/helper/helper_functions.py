# import os
# import csv
# from typing import List
# from uuid import uuid4
# from fastapi import FastAPI, HTTPException
# from routers import authors_router, loans_router, users_router, books_router
#
# app = FastAPI()
# app.include_router(authors_router)
# app.include_router(loans_router)
# app.include_router(users_router)
# app.include_router(books_router)
#
#
#
# def read_csv(file_path: str):
#     data = []
#     if not os.path.exists(file_path):
#         return data
#     try:
#         with open(file_path, newline='', encoding='utf-8') as f:
#             reader = csv.DictReader(f)
#             for row in reader:
#                 data.append(row)
#     except Exception as e:
#         print(f"Eroare la citirea fișierului {file_path}: {e}")
#     return data
#
# def write_csv(file_path: str, data: List[dict], fieldnames: List[str]):
#     try:
#         with open(file_path, 'w', newline='', encoding='utf-8') as f:
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(data)
#     except Exception as e:
#         print(f"Eroare la scrierea în fișierul {file_path}: {e}")
#
#
# USERS_FILE = 'db/users.csv'
#
#
# def get_users():
#     return read_csv(USERS_FILE)
#
# def add_user(user):
#     users = get_users()
#     if any(u['username'] == user.username for u in users):
#         raise HTTPException(status_code=400, detail="Utilizator deja existent")
#     users.append(user.dict())
#     write_csv(USERS_FILE, users, ['username', 'password'])
#
# def authenticate_user(username: str, password: str):
#     users = get_users()
#     for u in users:
#         if u['username'] == username and u['password'] == password:
#             return True
#     return False
#
#
# AUTHORS_FILE = 'db/authors.csv'
#
#
# def get_authors():
#     return read_csv(AUTHORS_FILE)
#
#
# def add_author(author):
#     authors = get_authors()
#     if any(a['name'] == author.name for a in authors):
#         raise HTTPException(status_code=400, detail="Autor deja existent")
#     authors.append(author.dict())
#     write_csv(AUTHORS_FILE, authors, ['id', 'name'])
#
#
# def search_author_by_name(name: str):
#     authors = get_authors()
#     return [a for a in authors if name.lower() in a['name'].lower()]
#
#
# BOOKS_FILE = 'db/books.csv'
#
#
# def get_books()
#     books = get_books()
#     book = next((b for b in books if b['id'] == loan['book_id']), None)
#     if book:
#         book['available'] = 'True'
#         write_csv(BOOKS_FILE, books, ['id', 'title', 'author_id', 'available'])
#
#
#
#
# def add_book(book):
#     books = get_books()
#     if any(b['title'] == book.title for b in books):
#         raise HTTPException(status_code=400, detail="Cartea deja există")
#     books.append(book.dict())
#     write_csv(BOOKS_FILE, books, ['id', 'title', 'author_id', 'available'])
#
#
# def search_books_by_title(title: str):
#     books = get_books()
#     return [b for b in books if title.lower() in b['title'].lower()]
#
#
# LOANS_FILE = 'db/loans.csv'
#
#
# def get_loans():
#     return read_csv(LOANS_FILE)
#
#
# # verificare carte imprumutata
# def add_loan(user: str, book_id: str):
#     books = get_books()
#     book = next((b for b in books if b['id'] == book_id), None)
#     # functia next returneaza primul element care indeplineste conditia
#     if not book:
#         raise HTTPException(status_code=404, detail="Cartea nu a fost găsită")
#     if book['available'] == 'False':
#         raise HTTPException(status_code=400, detail="Cartea nu este disponibilă")
#         # Marcare carte ca indisponibilă
#         book['available'] = 'False'
#         # Salvare cărți modificate
#         write_csv(BOOKS_FILE, books, ['id', 'title', 'author_id', 'available'])
#
#
#     # Salvare cărți modificate
#     write_csv(BOOKS_FILE, books, ['id', 'title', 'author_id', 'available'])
#
#     # Creare imprumut
#
#     loans = get_loans()
#     loan_id = str(uuid4())
#     loan = {'id': loan_id,
#             'user': user,
#             'book_id': book_id,
#             'returned': 'False',
#             }
#     loans.append(loan)
#     write_csv(LOANS_FILE, loans, ['id', 'user', 'book_id', 'returned'])
#     return
#
#
# def return_loan(loan_id: str):
#     loans = get_loans()
#     loan = next((l for l in loans if l['id'] == loan_id), None)
#     if not loan:
#         raise HTTPException(status_code=404, detail="Împrumut nu găsit")
#     if loan['returned'] == 'True':
#         raise HTTPException(status_code=400, detail="Cartea a fost deja returnată")
#     loan['returned'] = 'True'
#     # Actualizare fișier împrumuturi
#     write_csv(LOANS_FILE, loans, ['id', 'user', 'book_id', 'returned'])
#     # Actualizare disponibilitate carte
#     books = get_books(
#     if book:
#         book['available'] = 'True'
#     write_csv(BOOKS_FILE, books, ['id', 'title', 'author_id', 'available'])
#     return loan
#
#
# def get_top_books():
#     loans = get_loans()
#     books = get_books()
#     # Calcularea celor mai împrumutate cărți
#
#     count_dict = {}
#     for loan in loans:
#         if loan['returned'] == 'False':
#             continue
#         book_id = loan['book_id']
#         count_dict[book_id] = count_dict.get(book_id, 0) + 1
#     # Sortare după frecvență
#
#     sorted_books = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
#     top5_ids = [b[0] for b in sorted_books[:5]]
#     top_books = [b for b in books if b['id'] in top5_ids]
#     return top_books

import os
import csv
from typing import List
from uuid import uuid4
from fastapi import HTTPException


# Functie pentru citirea unui fișier CSV
def read_csv(file_path: str):
    data = []
    if not os.path.exists(file_path):  # Verificare existența fișierului
        return data
    try:
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"Eroare la citirea fișierului {file_path}: {e}")
    return data


# Functie pentru scrierea unui fișier CSV
def write_csv(file_path: str, data: List[dict], fieldnames: List[str]):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Eroare la scrierea în fișierul {file_path}: {e}")


# Fișierele CSV
USERS_FILE = 'db/users.csv'
AUTHORS_FILE = 'db/authors.csv'
BOOKS_FILE = 'db/books.csv'
LOANS_FILE = 'db/loans.csv'


# Funcții pentru utilizatori
def get_users():
    return read_csv(USERS_FILE)


def add_user(user):
    users = get_users()
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


# Funcții pentru autori
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


# Funcții pentru cărți
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


# Funcții pentru împrumuturi
def get_loans():
    return read_csv(LOANS_FILE)


def add_loan(user: str, book_id: str):
    books = get_books()
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Cartea nu a fost găsită")

    if not book['available']:  # Aici presupun că 'available' este un boolean
        raise HTTPException(status_code=400, detail="Cartea nu este disponibilă")

    # Marcare carte ca indisponibilă
    book['available'] = False
    # Salvare cărți modificate
    write_csv(BOOKS_FILE, books, ['id', 'title', 'author_id', 'available'])

    # Creare împrumut
    loans = get_loans()
    loan_id = str(uuid4())
    loan = {'id': loan_id, 'user': user, 'book_id': book_id, 'returned': False}
    loans.append(loan)
    write_csv(LOANS_FILE, loans, ['id', 'user', 'book_id', 'returned'])
    return loan


def return_loan(loan_id: str):
    loans = get_loans()
    loan = next((l for l in loans if l['id'] == loan_id), None)
    if not loan:
        raise HTTPException(status_code=404, detail="Împrumut nu găsit")

    if loan['returned']:
        raise HTTPException(status_code=400, detail="Cartea a fost deja returnată")

    loan['returned'] = True
    # Actualizare fișier împrumuturi
    write_csv(LOANS_FILE, loans, ['id', 'user', 'book_id', 'returned'])

    # Actualizare disponibilitate carte
    books = get_books()
    book = next((b for b in books if b['id'] == loan['book_id']), None)
    if book:
        book['available'] = True
    write_csv(BOOKS_FILE, books, ['id', 'title', 'author_id', 'available'])

    return loan


def get_top_books():
    loans = get_loans()
    books = get_books()

    count_dict = {}
    for loan in loans:
        if not loan['returned']:
            continue
        book_id = loan['book_id']
        count_dict[book_id] = count_dict.get(book_id, 0) + 1

    # Sortare după frecvență
    sorted_books = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    top5_ids = [b[0] for b in sorted_books[:5]]
    top_books = [b for b in books if b['id'] in top5_ids]
    return top_books


