from sqlalchemy import Integer, String,ForeignKey
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import DateTime
from datetime import datetime

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    username:Mapped[str]= mapped_column(String(20),unique=True,nullable=False)
    email:Mapped[str]= mapped_column(String(64),unique=True)
    password:Mapped[str]= mapped_column(String(64),nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"
    """definește cum va arăta un obiect de tip User atunci când este afișat/reprezentat,în consolă sau în listări"""

class Author(Base):
    __tablename__ = 'authors'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str]= mapped_column(String(20),unique=True,nullable=False)

    def __repr__(self):
        return f"Author('{self.name}')"

class Book(Base):
    __tablename__ = 'books'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str]= mapped_column(String(64),nullable=False)
    author_id:Mapped[int] = mapped_column(Integer,ForeignKey("authors.id"))
    total_copies: Mapped[int] = mapped_column(Integer, nullable=False)
    available_copies: Mapped[int] = mapped_column(Integer, nullable=False)


    def __repr__(self):
        return f"Book('{self.title}')"
class Loans(Base):
    __tablename__ = 'loans'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    book_id:Mapped[int] = mapped_column(Integer, ForeignKey("books.id"))
    loan_date:Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    return_date:Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Loan(book_id={self.book_id}, loan_date={self.loan_date}, return_date={self.return_date})"