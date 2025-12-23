from fastapi import FastAPI, status, Response
import json

app = FastAPI()


@app.post("/create-user")
def create_user(username: str, password: str, email: str, address: str, response: Response):

    with open("user_information_data.json") as f:
        data = json.load(f)
    
    for x in data:
        if x["username"] == username:
            response.status_code = status.HTTP_409_CONFLICT
            return {"message": "User with this username already exists"}

    new_user = {"username": username, "password": password, "email": email, "address": address}

    data.append(new_user)

    with open("user_information_data.json", "w") as f:
        json.dump(data, f, indent=4)

    response.status_code = status.HTTP_201_CREATED
    return {"message": "User created successfully"}


@app.get("/read-users")
def read_users():
    with open("user_information_data.json") as f:
        data =  json.load(f)
    return data    
    


@app.patch("/update-user")
def update_user(
    username: str,
    response: Response,
    password: str | None = None,
    email: str | None = None,
    address: str | None = None
):
    with open("user_information_data.json") as f:
        data = json.load(f)

    for x in data:
        if x["username"] == username:
            if password is not None:
                x["password"] = password
            if email is not None:
                x["email"] = email
            if address is not None:
                x["address"] = address

            with open("user_information_data.json", "w") as f:
                json.dump(data, f, indent=4)

            return {"message": "User updated successfully"}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "User not found"}


@app.delete("/delete-user")
def delete_user(username: str, response: Response):
    with open("user_information_data.json") as f:
        data = json.load(f)

    for x in data:
        if x["username"] == username:
            data.remove(x)
            with open("user_information_data.json", "w") as f:
                json.dump(data, f, indent=4)
            return {"message": "User deleted successfully"}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "User not found"}
