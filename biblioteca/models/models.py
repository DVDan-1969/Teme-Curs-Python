from pydantic import BaseModel



class Author(BaseModel):
    name: str
    id: str

class Book(BaseModel):
    id: str
    title: str
    author_id: str
    available:bool

class User(BaseModel):
    username: str
    password: str
    id:str

class Loans(BaseModel):
    id: str
    user: str
    book_id: str
    returned: bool








