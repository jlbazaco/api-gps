from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API GPS funcionando correctamente"}

@app.get("/saludo")
async def saludo(nombre: str = "Usuario"):
    return {"saludo": f"Hola, {nombre}"}

@app.post("/eco")
async def eco(data: dict):
    return {"recibido": data}

@app.exception_handler(Exception)
async def error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": str(exc)},
    )
