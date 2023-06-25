from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.config import engine
from core import blog, user, auth
from models import models
from settings import DEBUG

models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="NovaAPI",
    description="API For Personal Blog",
    version="1.2.0",

    docs_url=None if DEBUG == False else '/docs',
    redoc_url=None if DEBUG == False else '/redoc'
    )


origins = [
    "*" # not recommended for production unless you know what you are doing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)
