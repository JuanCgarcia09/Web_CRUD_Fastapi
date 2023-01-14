from fastapi import FastAPI
from routers import products,users,auth_users
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#   Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(auth_users.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#   Static sources
app.mount("/static",StaticFiles(directory="Static"),name="static")

@app.get("/")
async def root():
    return "Hola FastAPI"
@app.get("/url")

async def url():
    return {"url_curso":"https://mourdev.com/python"}
