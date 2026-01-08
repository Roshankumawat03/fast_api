from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Body
from sqlmodel import SQLModel, Field, create_engine, Session, select
import bcrypt



class Hero(SQLModel, table= True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()
    username: str = Field(unique=True, nullable=False)
    mob: str = Field(unique=True, nullable=False)
    age: int 
    password: str = Field(nullable=False)


sqlite_url = f"sqlite:///database.db"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "This is home page."}

@app.post("/register")
def register(db: SessionDep, data = Body(...)):
    password = bcrypt.hashpw(data.get("password").encode("UTF-8"), salt=bcrypt.gensalt(14))
    data_for_entry = Hero(
        name=data.get("name"),
        username=data.get("username"),
        mob=data.get("mob"),
        age=data.get("age"),
        password=password
    )
    db.add(data_for_entry)
    db.commit()
    return {"message": data}


@app.post("/get_all_data")
def register(db : SessionDep):
    test = db.query(Hero).all()
    return {"message": test}


@app.get("/get/{username}")
def register(username,db : SessionDep):

    test = db.query(Hero).filter(Hero.username == username).first()
    if not test:
        return HTTPException(409, "User not found.")


@app.patch("/update/{username}")
def update(username, db : SessionDep, data = Body(...)):

    data_in_db = db.query(Hero).filter(Hero.username == username).first()
    if not data_in_db:
        return HTTPException (409, "User not found.")
    
    if data.get("password"):
        password = bcrypt.hashpw(data.get("password").encode("UTF-8"), salt=bcrypt.gensalt(14))
        data_in_db.password = password
    if  data.get("name"):
        data_in_db.name = data.get("name")
    if data.get("mob"):
        data_in_db.mob =data.get("mob")
    if data.get("age"):
        data_in_db.age = data.get("age")

    db.add(data_in_db)
    db.commit()    

    return {"message": "User updated completed."} 


@app.patch("/delete/{id}")
def delete(id, db : SessionDep):

    data_in_db = db.query(Hero).filter(Hero.id == id).first()
    if not data_in_db:
        return HTTPException (409, "User not found.")
    

    db.delete(data_in_db)
    db.commit()    

    return {"message": "User deleted completed."}
