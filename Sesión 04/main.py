from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum

#instaciamos la clase FastAPI
app = FastAPI()

#Creamos nuestro primer modelo
class Post(BaseModel):
    author: str
    title: str
    content: str

class Role(str, Enum):
    admin = "admin"
    user = "user"

#Creamos el user
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    city: str
    roles: List[Role]


@app.get("/")
async def root():
    return{"name": "Alonso Guillén"}

@app.get("/posts/{id}")
async def getPost(id):
    return {"data": id}

@app.post("/posts")
async def viewPost(post: Post):
    return {"alerta": f"El post de {post.title} ha sido agregado a la biblioteca."}

@app.post("/api/v1/add_user")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.get("/api/v1/users")
def get_all_users():
    return db

@app.delete("/api/v1/delete_user/{id}")
def delete_user(id: UUID):
    for user in db:
        if user.id==id:
            db.remove(user)
            return {"message": f"El usuario {user.first_name} {user.last_name} ha sido eliminado."}

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Freddy",
        last_name="Nolasco",
        city="Lima",
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Juan",
        last_name="Falcón",
        city="Trujillo",
        roles=[Role.admin]
    ),
    User(
        id=uuid4(),
        first_name="Noelia",
        last_name="Pérez",
        city="Lima",
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Edwin",
        last_name="Deza",
        city="Cusco",
        roles=[Role.admin, Role.user]
    )
]