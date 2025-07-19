from typing import Optional
from fastapi import FastAPI,Header
from pydantic import BaseModel
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}   

@app.get("/greet/")
async def greet(name: Optional[str] = "user", age: Optional[int] = 0):
    return {"Hello": name, "Age": age}

class BookCreateModel(BaseModel):
    title: str
    author: str
    year: int

@app.post("/create_book/")
async def create_book(book: BookCreateModel):
    return {
        "title": book.title,
        "author": book.author,
    }

@app.get("/get_header", status_code=200)
async def get_headers(
    accept:str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None)
):
    request_headers = {}
    
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    return  request_headers