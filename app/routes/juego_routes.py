from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers.lectura_controller import LecturaController
from app.schemas.lectura import PalabraResponse, ValidacionRequest, ValidacionResponse

router = APIRouter(prefix="/juego", tags=["juego"])

@router.get("/{lectura_id}/palabra", response_model=PalabraResponse)
def obtener_palabra_actual(
    lectura_id: int,
    usuario_id: str,
    db: Session = Depends(get_db)
):
    """
    Obtiene la siguiente palabra de la lectura para el usuario
    """
    return LecturaController.obtener_palabra_actual(db, lectura_id, usuario_id)

@router.post("/{lectura_id}/validar", response_model=ValidacionResponse)
def validar_palabra(
    lectura_id: int,
    request: ValidacionRequest,
    db: Session = Depends(get_db)
):
    """
    Valida la palabra ingresada por el usuario contra la palabra actual
    """
    return LecturaController.validar_palabra(
        db, 
        lectura_id, 
        request.usuario_id, 
        request.palabra
    )