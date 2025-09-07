from pydantic import BaseModel

class User:
    def __init__(self, id: int, name:str , email:str):
        self.id = id
        self.name = name
        self.email = email

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str


