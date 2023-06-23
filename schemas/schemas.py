from pydantic import BaseModel
from pydantic.main import BaseConfig

class PostBase(BaseModel):
    title: str
    content: str

class Post(PostBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    username: str
    password: str

class ShowUser(BaseModel):
    username: str
    posts: list[Post] = []

    class Config():
        orm_mode = True

class ShowPost(BaseModel):
    title: str
    content: str
    # creator: ShowUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str