from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Modelo para recibir datos GPS
class GPSData(BaseModel):
    lat: float
    lon: float
    timestamp: datetime

@app.get("/")
async def root():
    return {"message": "API GPS funcionando correctamente"}

@app.get("/saludo")
async def saludo(nombre: str = "Usuario"):
    return {"saludo": f"Hola, {nombre}"}

@app.post("/eco")
async def eco(data: dict):
    return {"recibido": data}

@app.post("/gps")
async def recibir_gps(data: GPSData):
    return {
        "status": "OK",
        "received": {
            "lat": data.lat,
            "lon": data.lon,
            "timestamp": data.timestamp.isoformat()
        }
    }

@app.exception_handler(Exception)
async def error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": str(exc)},
    )
