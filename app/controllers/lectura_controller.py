from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.lectura import Lectura
from typing import Dict

class LecturaController:
    # Estado de progreso por usuario (en memoria)
    _progreso_usuarios: Dict[str, Dict[int, int]] = {}  # {user_id: {lectura_id: indice}}
    _aciertos_usuarios: Dict[str, Dict[int, int]] = {}  # {user_id: {lectura_id: aciertos}}

    @staticmethod
    def get_lectura(db: Session, lectura_id: int):
        """Obtiene una lectura por su ID"""
        lectura = db.query(Lectura).filter(Lectura.id == lectura_id).first()
        if not lectura:
            raise HTTPException(status_code=404, detail="Lectura no encontrada")
        return lectura

    @staticmethod
    def get_lecturas(db: Session, skip: int = 0, limit: int = 100):
        """Obtiene todas las lecturas"""
        return db.query(Lectura).offset(skip).limit(limit).all()

    @staticmethod
    def obtener_palabra_actual(db: Session, lectura_id: int, usuario_id: str):
        """Obtiene la siguiente palabra para el usuario"""
        lectura = LecturaController.get_lectura(db, lectura_id)
        palabras = lectura.contenido.split()
        
        # Inicializar progreso si es nuevo usuario/lectura
        if usuario_id not in LecturaController._progreso_usuarios:
            LecturaController._progreso_usuarios[usuario_id] = {}
            LecturaController._aciertos_usuarios[usuario_id] = {}
        
        if lectura_id not in LecturaController._progreso_usuarios[usuario_id]:
            LecturaController._progreso_usuarios[usuario_id][lectura_id] = 0
            LecturaController._aciertos_usuarios[usuario_id][lectura_id] = 0

        indice = LecturaController._progreso_usuarios[usuario_id][lectura_id]
        
        if indice >= len(palabras):
            return {
                "palabra": None,
                "indice": indice,
                "fin_lectura": True,
                "total_palabras": len(palabras)
            }
        
        palabra = palabras[indice]
        return {
            "palabra": palabra,
            "indice": indice,
            "fin_lectura": False,
            "total_palabras": len(palabras)
        }

    @staticmethod
    def validar_palabra(db: Session, lectura_id: int, usuario_id: str, palabra: str):
        """Valida la palabra del usuario"""
        lectura = LecturaController.get_lectura(db, lectura_id)
        palabras = lectura.contenido.split()
        
        # Obtener índice actual
        indice = LecturaController._progreso_usuarios.get(usuario_id, {}).get(lectura_id, 0)
        
        if indice >= len(palabras):
            raise HTTPException(status_code=400, detail="La lectura ya ha terminado")
        
        palabra_correcta = palabras[indice]
        es_correcta = palabra.lower() == palabra_correcta.lower()
        
        # Actualizar progreso y aciertos
        LecturaController._progreso_usuarios[usuario_id][lectura_id] = indice + 1
        if es_correcta:
            LecturaController._aciertos_usuarios[usuario_id][lectura_id] += 1
        
        # Obtener siguiente palabra
        siguiente = LecturaController.obtener_palabra_actual(db, lectura_id, usuario_id)
        
        return {
            "es_correcta": es_correcta,
            "palabra_correcta": palabra_correcta,
            "siguiente_palabra": siguiente,
            "progreso": (indice + 1) / len(palabras)
        }

    @staticmethod
    def obtener_resumen(db: Session, lectura_id: int, usuario_id: str):
        """Genera resumen del progreso del usuario"""
        lectura = LecturaController.get_lectura(db, lectura_id)
        palabras_totales = len(lectura.contenido.split())
        palabras_acertadas = LecturaController._aciertos_usuarios.get(usuario_id, {}).get(lectura_id, 0)
        
        return {
            "lectura_id": lectura_id,
            "palabras_totales": palabras_totales,
            "palabras_acertadas": palabras_acertadas,
            "precision": palabras_acertadas / palabras_totales if palabras_totales > 0 else 0
        }