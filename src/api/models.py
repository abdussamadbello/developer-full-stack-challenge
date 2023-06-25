from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, MetaData, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from alembic import op


Base = declarative_base(metadata=MetaData())

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    number_of_pages = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))
