import os
import csv
from uuid import uuid4
from typing import List, Optional
from fastapi import Request, HTTPException
from fastapi import FastAPI
from routers import authors_router,loans_router,users_router,books_router
app = FastAPI()

app.include_router(users_router)
app.include_router(authors_router)
app.include_router(books_router)
app.include_router(loans_router)
























