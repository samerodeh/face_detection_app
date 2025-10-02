from pydantic import BaseModel


class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserEmbeddings(BaseModel): 
    name: str
    embedding: list[float]



























    