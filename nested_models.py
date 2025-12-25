from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    username: str
    age: int


class Task(BaseModel):
    title: str
    desc: str
    user: list[User]
    

app = FastAPI()

@app.get("/test/{data}")
def create_item(data):
    return data

@app.get("/test_qp/")
def create_item(data):
    return data

@app.post("/items/")
def create_item(data: Task):
    return data

