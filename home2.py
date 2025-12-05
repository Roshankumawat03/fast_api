from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/users")
def user():
    with open ("dummy_user_data.json") as f:
        data = json.load(f)
    final_data = []
    data = data["users"]
    for x in data:
        final_data.append(x.get("lastName"))
    return final_data

@app.get("/email")
def email():
    with open ("dummy_user_data.json") as f:
        data = json.load(f)
    email_address = []
    data = data["users"]
    for x in data:
        email_address.append(x.get("email"))
    return email_address

@app.get("/hair")
def hair():
    with open ("dummy_user_data.json") as f:
        data = json.load(f)
    hair_color = []
    data = data["users"]
    for x in data:
        hair_color.append(x.get("hair")["color"])
    return hair_color   

@app.get("/city_names")
def city_names():
    with open ("dummy_user_data.json") as f:
        data = json.load(f)
    all_city_names = []
    data = data["users"]
    for x in data:
        add_dict = x.get("address")
        all_city_names.append(add_dict["city"])
    return all_city_names   

@app.get("/coordinates")
def coordinates():
    with open ("dummy_user_data.json") as f:
        data = json.load(f)
    coordinates = []
    data = data["users"]
    for x in data:
        add_dict = x.get("address")
        coordinates.append(add_dict["coordinates"]["lng"])
    return coordinates

@app.get("/bank")
def bank():
    with open ("dummy_user_data.json") as f:
        data = json.load(f)
    bank_currency = []
    data = data["users"]
    for x in data:
        add_dict = x.get("bank")
        bank_currency.append(add_dict["currency"])
    return bank_currency 

@app.get("/name_email")
def name_email():
    with open ("dummy_user_data.json") as f:
        data = json.load(f)
    name_email = []
    data = data["users"]
    for x in data:
        name_email.append(
            {
            "name": x.get("firstName"), 
            "mail": x.get("email")
            })
    return name_email                            
       
