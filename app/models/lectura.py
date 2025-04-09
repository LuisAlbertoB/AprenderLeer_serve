from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Lectura(Base):
    __tablename__ = "lecturas"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre_libro = Column(String(100), nullable=False)
    autor = Column(String(100), nullable=False)
    capitulo = Column(Integer)
    contenido = Column(Text, nullable=False)  # Texto completo del capítulo
    
    # Relación con Audio (opcional)
    audios = relationship("Audio", back_populates="lectura")