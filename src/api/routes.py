from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from authentication import *
from database import *
import schemas
from models import *
from typing import List
import logging

logger = logging.getLogger("uvicorn.info")

auth_router = APIRouter()

@auth_router.post("/login")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    logger.info( user,"user", form_data.username, "username", form_data.password, "password")
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.get("/token")
def validate_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return verify_token(token, db)

books_router = APIRouter(
    prefix="/books",
    tags=["books"],
    dependencies=[Depends(verify_token)],
)

@books_router.get("/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(Book).offset(skip).limit(limit).all()
    return books

@books_router.post("/", response_model=schemas.Book)
def create_book(book: schemas.Book, db: Session = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@books_router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@books_router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.Book, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db_book.name = book.name
    db_book.author_id = book.author_id
    db_book.number_of_pages = book.number_of_pages
    db.commit()
    db.refresh(db_book)
    return db_book

@books_router.delete("/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return db_book

@books_router.get("/search/{book_name}", response_model=List[schemas.Book])
def search_book(book_name: str, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.name.like("%" + book_name + "%")).all()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

authors_router = APIRouter(
    prefix="/authors",
    tags=["authors"],
    dependencies=[Depends(verify_token)],
)

@authors_router.get("/")
def read_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    authors = db.query(Author).offset(skip).limit(limit).all()
    return authors

@authors_router.post("/")
def create_author(author: schemas.Author, db: Session = Depends(get_db)):
    db_author = Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

@authors_router.get("/{author_id}")
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

@authors_router.put("/{author_id}")
def update_author(author_id: int, author: schemas.Author, db: Session = Depends(get_db)):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    db_author.name = author.name
    db.commit()
    db.refresh(db_author)
    return db_author

@authors_router.delete("/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(db_author)
    db.commit()
    return db_author

@authors_router.get("/search/{author_name}")
def search_author(author_name: str, db: Session = Depends(get_db)):
    db_author = db.query(Author).filter(Author.name.like("%" + author_name + "%")).all()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

@authors_router.get("/search/{author_name}/{book_name}")
def search_author_book(author_name: str, book_name: str, db: Session = Depends(get_db)):
    db_author = db.query(Author).filter(Author.name.like("%" + author_name + "%")).all()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    db_book = db.query(Book).filter(Book.name.like("%" + book_name + "%")).all()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_author, db_book

@authors_router.get("/number_of_books/{author_id}")
def number_of_books(author_id: str, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.author_id == author_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Author/book not found")
    # count number of pages in all books
    total_pages = sum([book.number_of_pages for book in db_book])
    return total_pages

