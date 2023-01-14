from fastapi import APIRouter, Depends,HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestForm, OAuth2PasswordBearer

oauth2 = OAuth2PasswordBearer(tokenUrl="login")
router = APIRouter(prefix="/basicauth", tags=["basicauth"], responses={404: {"message" : "no encontrado"}})


class user(BaseModel):
    username : str
    full_name : str
    email : str
    disable : bool

class user_db(user):
    password: str

users_db = {
    "Juancgarcia": {
        "username": "Juancgarcia",
        "full_name" : "Juan Garcia",
        "email": "Juancamilogarcia0930@gmail.com",
        "disable" : False,
        "password" : "123456"
    },    
    "Juancgarcia2": {
        "username": "Juancgarcia2",
        "full_name" : "Juan Garcia2",
        "email": "Juancamilogarcia09320@gmail.com",
        "disable" : True,
        "password" : "1234526"
    }
}




def search_user_db(username : str):
    if username in users_db:
        return user_db(**users_db[username])

def search_user(username : str):
    if username in users_db:
        return user(**users_db[username])


async def current_user(token : str = Depends(oauth2)):
    User = search_user(token)
    if not User:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación invalida", headers={"WWW-Authenticate": "Bearer"})
    if User.disable:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación invalida", headers={"WWW-Authenticate": "Bearer"})
    return User

@router.post("/login")
async def login(form : OAuth2PasswordRequestForm = Depends()):
    User_db = users_db.get(form.username)
    if not User_db:
        raise HTTPException(status_code=404, detail="El usuario no se ha encontrado")
    usuario = search_user_db(form.username)
    if not form.password == usuario.password:
        raise HTTPException(status_code=404, detail="La contraseña no es valida")
    return {"access_token": usuario.username , "token_type" : "bearer"}

@router.get("/users/me")
async def me(usuario: user = Depends(current_user)):
    return usuario