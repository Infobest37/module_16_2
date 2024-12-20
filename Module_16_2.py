from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel
# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def root():
    return "Главная страница"
@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"

@app.get("/user/{password}")
async def news(password: int) -> str:
    return f"Вы вошди как пользователь № {password}"

@app.get("/user")
async def user(username: str = Path(min_length=5,max_length=20, description="Enter username", example="EvgenUser"),
               age: int = Path(min_length=18, max_length=120,description="Enter age", example= 32 )) -> str:
     return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
@app.get("/user/user_id{}")
async def user(user_id: Annotated[int, Path(min_length= 1, max_length=100, description="Enter User ID", example= 74 )]) -> str:
     return f"Информация о пользователе. Имя: {user_id}"