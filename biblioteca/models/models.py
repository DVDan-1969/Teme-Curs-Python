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


class Loans(BaseModel):
    id: str
    username: str
    book_id: str
    returned: bool








