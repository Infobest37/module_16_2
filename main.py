from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def root():
    return {"message": "Hello Worl"}


@app.get("/usertest/A/B")
async def news() -> dict:
    return {"message": f"Привет я свой"}


@app.get("/user/{username}/{id}")

    # '''"Это прописывается когда нужно прописывать два параметра user name and id'''
# async def news(username: str = Path(min_length=3, max_length=15, description="Enter your username"),
#                id: int = Path(ge=0, le=100, description="Enter your id", example="74")) -> dict:
#     return {"message": f"Hello {username} {id}"}

    #'''Но когда нам нужно прописать только один параметр а другой оставить без описания нужно использовать Annotated'''
async def news_get(username: Annotated[str, Path(min_length=3, max_length=15, description="Enter your username")],
                       id: int ):
    return {"message": f"Hello {username} {id}"}

@app.get("/id")
async def news_id(username: str, age: int) -> dict:
    return {"User": username, "Age": age}