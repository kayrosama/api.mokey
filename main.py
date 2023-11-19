from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.bdd import engine, Base
from routers.app_routes import reg_router

app = FastAPI()
app.title = "ksmflypkg" #Nombre de la aplicacion.
app.version = "0.0.1" #Version de la aplicacion.

app.include_router(reg_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>WTF</h1')
