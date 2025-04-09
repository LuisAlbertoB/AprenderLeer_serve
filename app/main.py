from fastapi import FastAPI
from app.routes import lectura_routes, juego_routes

app = FastAPI(
    title="AprenderLeer API",
    version="0.1",
    description="API para el juego de aprendizaje de lectura"
)

# Incluir rutas
app.include_router(lectura_routes.router)
app.include_router(juego_routes.router)

@app.get("/", tags=["Root"])
def home():
    return {"message": "API activa!"}