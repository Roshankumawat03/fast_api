from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    roll_number: str
    stream: str
    mob: str
    password: str

class Takeinput(BaseModel):
    name: str
    age: int

@app.post("/login/")
async def login(data: Annotated[Student, Form()]):
    return data

@app.post("/test/")
async def login(a, b):
    return a

@app.post("/check_eligibility_post/")
def test(data: Annotated[Takeinput, Form()]):
    return data.age
