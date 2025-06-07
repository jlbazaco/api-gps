from fastapi import FastAPI, Request
import pyodbc
from datetime import datetime

app = FastAPI()

# Conexión a SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=BZX-TECH;DATABASE=MISPRUEBAS2;Trusted_Connection=yes;'
)
cursor = conn.cursor()

@app.post("/api/gps")
async def recibir_gps(request: Request):
    data = await request.json()
    dispositivo = data.get("dispositivo")
    lat = data.get("latitud")
    lon = data.get("longitud")
    fecha = data.get("fecha", datetime.now().isoformat())

    cursor.execute("""
        INSERT INTO dbo.PosicionesGPS (dispositivo, latitud, longitud, fecha)
        VALUES (?, ?, ?, ?)
    """, dispositivo, lat, lon, fecha)

    conn.commit()
    return {"status": "ok", "mensaje": "Datos guardados"}