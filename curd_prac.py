from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class Transport(BaseModel):
    dr_name: str
    tr_description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.get("/test/{data}")
def create_item(data):
    return data

@app.get("/test_qp/")
def create_item(data):
    return data

@app.post("/items/")
def create_item(item: Item, tf: Transport):
    return [item, tf]

