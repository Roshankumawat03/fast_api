from fastapi import FastAPI, status, Response
import json
from pydantic import BaseModel

app = FastAPI()

class User( BaseModel ):
    username: str
    name: str = None
    mail: str = None
    addr: str = None
    mob: int = None

def read_file():
    with open("user_app_database.json") as f:
        existing_data = json.load(f)
    return existing_data

def write_file(data):
    with open("user_app_database.json", "w") as f:
        json.dump(data, f, indent=4)


@app.post("/create")
def create(data: User, response:Response):

    existing_data = read_file()
    for x in existing_data:
        if x.get("username") == data.username:
            response.status_code = status.HTTP_409_CONFLICT
            return{"message": "username alredy available."}
        
    existing_data.append({
        "username": data.username,
        "name": data.name,
        "mail": data.mail,
        "addr": data.addr,
        "mob": data.mob
    })
    write_file(existing_data)
    return {"message": "User created successfully."}


@app.put("/update")
def update(data: User, response:Response):

    existing_data = read_file()
    for x in existing_data:
        if x["username"] == data.username:
            if data.name:
                x["name"] = data.name
            if data.mail:
                x["mail"] = data.mail
            if data.addr:    
                x["addr"] = data.addr
            if data.mob:    
                x["mob"] = data.mob
            write_file(existing_data)
            return{"message": "username updated done."}

    response.status_code = status.HTTP_409_CONFLICT
    return{"message": "username not available."}


@app.get("/read")
def read():

    existing_data = read_file()
    return existing_data


@app.delete("/delete")
def delete(username:str, response:Response):

    existing_data = read_file()
    for x in existing_data:
        if x["username"] == username:
            existing_data.remove(x)
            write_file(existing_data)
            return{"message": "username deleted successfully"}

    response.status_code = status.HTTP_409_CONFLICT
    return{"message": "username not available."}       
   
    
