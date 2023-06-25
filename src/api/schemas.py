from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    username: str
    hashed_password: str
    disabled: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class Author(BaseModel):
    id: int
    name: str = Field(..., description="This field is required")

    class Config:
        orm_mode = True

class Book(BaseModel):
    id: int
    name: str = Field(..., description="This field is required")
    author_id: int = Field(..., description="This field is required")
    number_of_pages: int
    
    class Config:
        orm_mode = True
