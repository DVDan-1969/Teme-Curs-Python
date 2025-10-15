
from fastapi import FastAPI
from database import engine
from models import Base

# Importă routerele
from routes.authors import router as author_router
from routes.books import router as book_router
from routes.loans import router as loan_router
from routes.users import router as user_router


app = FastAPI()

# Creează tabelele în DB
Base.metadata.create_all(bind=engine)

# Înregistrează rutele
app.include_router(author_router)
app.include_router(book_router)
app.include_router(loan_router)
app.include_router(user_router)
