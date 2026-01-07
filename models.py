from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select

app = FastAPI()

class Hero(SQLModel, table= True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()
    age: int | None = Field()
    secret_name: str


sqlite_url = f"sqlite:///database.db"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session