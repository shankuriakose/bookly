from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"

app = FastAPI(
    title="Bookly API",
    description="An API for managing books",
    version=version,
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])