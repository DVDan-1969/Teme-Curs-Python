
from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    email: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    class Config:
        orm_mode = True

class BookCreate(BaseModel):
    title: str
    author_id: int
    total_copies: int = 1

class BookOut(BaseModel):
    id: int
    title: str
    available_copies: int
    class Config:
        orm_mode = True

class AuthorCreate(BaseModel):
    name: str

class AuthorOut(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class LoanCreate(BaseModel):
    book_id: int

class LoanOut(BaseModel):
    id: int
    book_id: int
    loan_date: datetime
    return_date: datetime | None
    class Config:
        orm_mode = True



