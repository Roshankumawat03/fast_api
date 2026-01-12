from src import task, users, models, auth, task
from fastapi import FastAPI

app = FastAPI()

app.include_router(users.user_routes)
app.include_router(auth.login_logout)
app.include_router(task.task_route)