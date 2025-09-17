from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Author(BaseModel):
    name: str
    id: str

class Book(BaseModel):
    id: str
    title: str
    author_id: str
    available: bool=True

class Loan(BaseModel):
    id: str
    user:str
    book_id: str
    returned: bool=False




