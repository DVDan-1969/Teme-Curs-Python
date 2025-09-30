from pydantic import BaseModel



class Author(BaseModel):
    name: str
    id: str

class Book(BaseModel):
    id: str
    title: str
    author_id: str
    available:bool






