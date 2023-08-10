from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers.router import reg

app = FastAPI()
app.title = "api.mokey"
app.version = "0.0.1"

app.include_router(reg)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World</h1')