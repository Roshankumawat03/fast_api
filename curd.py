from fastapi import FastAPI, status, Response
import json

app = FastAPI()

@app.post("/create")
def create_task( task_title: str , response: Response ,completed: bool = False, ):

    with open ("todo_app_database.json") as f:
        existing_data = json.load(f)

    data_dict = {
        "title": task_title,
        "completed": completed
    }

    for x in existing_data:
        if task_title == x.get("title"):
            response.status_code = status.HTTP_406_NOT_ACCEPTABLE
            return {"message": "A title with this name is already existed."}

    existing_data.append(data_dict)

    with open ("todo_app_database.json", "w") as f:
        json.dump(existing_data, f, indent=4)

    response.status_code = status.HTTP_201_CREATED
    return {"message": "Task added to the TO-DO list."}

@app.patch("/update")
def update_task( completed: bool ,response: Response,title: str = ""):

    with open("todo_app_database.json") as f:
        existing_data = json.load(f)

    for x in existing_data:
        if title == x.get("title"):
            x["completed"] = completed
            with open ("todo_app_database.json", "w") as f:
                json.dump(existing_data, f, indent=4)
            return {"message": f"{title} is marked as {completed}."}
    
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "Title not found."}

@app.get("/read")
def read_data():
    
    with open("todo_app_database.json") as f:
        existing_data = json.load(f)
    
    return existing_data 

@app.delete("/delete")
def delete(response: Response,title: str = ""):

    with open("todo_app_database.json") as f:
        existing_data = json.load(f)

    for x in existing_data:
        if title == x.get("title"):
            existing_data.remove(x)
            with open ("todo_app_database.json", "w") as f:
                json.dump(existing_data, f, indent=4)
                return{"message": "data deleted"}

    Response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "Title not found."}           