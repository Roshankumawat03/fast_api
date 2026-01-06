from typing import Annotated

from fastapi import Depends, FastAPI, Response, status, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import datetime, jwt
from datetime import timezone, timedelta

app = FastAPI()

SECRET_KEY = "fjgnfxckj"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.get("/login")
def login(data: Annotated[OAuth2PasswordRequestForm, Depends()], response:Response):
    if data.username == "admin" and data.password == "123":
        return {
            "access_token": jwt.encode({"username": "admin", "exp": datetime.datetime.now() + timedelta(minutes=15)}, SECRET_KEY), 
            "refresh_token": jwt.encode({"username": "admin", "exp": datetime.datetime.now() + timedelta(hours=2)}, SECRET_KEY), 
            "token_type": "bearer"
        }
    else:
        Response.status_code = status.HTTP_401_UNAUTHORIZED
        return{"message": "login fail"}


def verify(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        jwt.decode(token, SECRET_KEY, ALGORITHM)
        return "Valid Token Found."
    except:
        HTTPException(401, "Unauthorized user.")


@app.post("/verify_token")
def verifyed(token: str):
    try:
        jwt.decode(token, SECRET_KEY, ALGORITHM)
        return "Valid Token Found."
    except:
        return HTTPException(401, "Unauthorized user.")

@app.get("/items/")
def read_items(data_form_login_api: Annotated[str, Depends(verify)]):
    return {"data_form_login_api": data_form_login_api}


@app.get("/home")
def read_items(data_form_login_api: Annotated[str, Depends(verify)]):
    return {"message": "Home page"}


@app.get("/")
def home():
    return HTMLResponse("""
    <h1>Hi</h1>
    <h2>Hi</h2>
    """)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt