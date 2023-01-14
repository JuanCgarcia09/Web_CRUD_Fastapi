from fastapi import APIRouter,HTTPException
from pydantic import BaseModel

#Entidad User
class user(BaseModel):
    id : int
    name : str
    surname : str
    url : str
    age : int

users_list = [user(id=1,name="Juan",surname="Elmago",url="https://www.elpepe.com",age=32),user(id=2,name="Pablito",surname="OOE",url="https://www.elpepe.sacom",age=11),user(id=3,name="Pedro",surname="Elmasad",url="https://www.elpesdpe.com",age=23)]

router = APIRouter(prefix="/users", tags=["users"], responses={404: {"message" : "no encontrado"}})

@router.get("/")
async def usersjson():
    return users_list

@router.get("/{id}")
async def User(id : int):
    return search_user(id)

@router.get("/users")
async def User(id : int):
    return search_user(id)

@router.post("/",status_code=201)
async def User(Usuario : user):
    if type(search_user(Usuario.id)) == user:
        raise HTTPException(status_code=204, detail="El usuario ya existe")
    else:
        users_list.routerend(Usuario)
        return(Usuario)

@router.put("/")
async def User(Usuario : user):
    found = False
    for index,saved_user in enumerate(users_list):
        if saved_user.id == Usuario.id:
            users_list[index] = Usuario
            found = True
    if not found:
        return{"Error": "No se ha actualizado el usuario"}


@router.delete("/{id}")
async def User(id : int):
    found = False
    for index,saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return{"Error": "No se ha eliminado el usuario"}

def search_user(id : int):
    usuarios = filter(lambda user:user.id == id,users_list)
    try:
        return list(usuarios)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}