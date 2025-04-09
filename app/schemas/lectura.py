from pydantic import BaseModel
from typing import Optional

class LecturaBase(BaseModel):
    nombre_libro: str
    autor: str

class LecturaCreate(LecturaBase):
    contenido: str
    capitulo: Optional[int] = None

class LecturaSchema(LecturaBase):
    id: int
    capitulo: Optional[int]
    contenido: str

    class Config:
        orm_mode = True

class PalabraResponse(BaseModel):
    palabra: Optional[str]
    indice: int
    fin_lectura: bool
    total_palabras: int

class ValidacionRequest(BaseModel):
    usuario_id: str
    palabra: str

class ValidacionResponse(BaseModel):
    es_correcta: bool
    palabra_correcta: str
    siguiente_palabra: PalabraResponse
    progreso: float

class ResumenLectura(BaseModel):
    lectura_id: int
    palabras_totales: int
    palabras_acertadas: int
    precision: float

    class Config:
        orm_mode = True