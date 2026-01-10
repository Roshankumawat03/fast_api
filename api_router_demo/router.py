from src import users, models, auth
from fastapi import FastAPI

app = FastAPI()

app.include_router(users.user_routes)
app.include_router(auth.login_logout)