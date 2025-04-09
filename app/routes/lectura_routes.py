from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers.lectura_controller import LecturaController
from app.schemas.lectura import LecturaSchema, ResumenLectura

router = APIRouter(prefix="/lecturas", tags=["lecturas"])

@router.get("/", response_model=list[LecturaSchema])
def listar_lecturas(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """
    Obtiene todas las lecturas disponibles
    """
    return LecturaController.get_lecturas(db, skip=skip, limit=limit)

@router.get("/{lectura_id}", response_model=LecturaSchema)
def obtener_lectura(
    lectura_id: int, 
    db: Session = Depends(get_db)
):
    """
    Obtiene una lectura específica por ID
    """
    return LecturaController.get_lectura(db, lectura_id)

@router.get("/{lectura_id}/resumen", response_model=ResumenLectura)
def obtener_resumen_lectura(
    lectura_id: int,
    usuario_id: str,
    db: Session = Depends(get_db)
):
    """
    Obtiene el resumen de progreso para una lectura y usuario
    """
    return LecturaController.obtener_resumen(db, lectura_id, usuario_id)