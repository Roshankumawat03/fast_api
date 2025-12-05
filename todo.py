from fastapi import FastAPI

file = FastAPI()

@file.get("/completed_todos")
def todos():
    return {"title":"todolist"}
