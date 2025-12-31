from typing import Annotated

from fastapi import Depends, FastAPI, Response, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Dummy(BaseModel):
    username: str
    password: str
    client_id: str


@app.get("/login")
def login(data: Annotated[Dummy, Form()], response:Response):
    if data.username == "admin" and data.password == "123":
        return {"message": "Login done"}
    else:
        Response.status_code = status.HTTP_401_UNAUTHORIZED
        return{"message": "login fail"}

@app.get("/items/")
def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}