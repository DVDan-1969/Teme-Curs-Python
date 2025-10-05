

from fastapi import FastAPI
from routers import authors_router,books_router,users_router,loans_router


app = FastAPI()

# Includ routerele în aplicație

app.include_router(authors_router)
app.include_router(books_router)
app.include_router(users_router)
app.include_router(loans_router)


