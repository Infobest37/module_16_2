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

# @app.get("/user/{password}")
# async def news(password: int) -> str:
#     return f"Вы вошди как пользователь № {password}"

@app.get("/user/{username}/{age}")
async def user(username: Annotated[str, Path(min_length=5, max_length=20,
                                             description="Enter username", example="EvgenUser")],
               age: Annotated[int, Path(ge=18, le=120, description="Enter age", example= 32 )]) -> str:

    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


@app.get("/users/{user_id}")
async def user_id(user_id: Annotated[int, Path(min_length=1,
                                            max_length=100, description="Enter User ID", example= 74 )]) -> str:
     return f"Информация о пользователе. Имя: {user_id} "