from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Audio(Base):
    __tablename__ = "audios"
    
    id = Column(Integer, primary_key=True, index=True)
    transcripcion = Column(String(200), nullable=False)  # Palabra/frase
    ruta_audio = Column(String(255), nullable=False)    # Ej: "/audios/hola.mp3"
    
    # Relación con Lectura (opcional)
    lectura_id = Column(Integer, ForeignKey("lecturas.id"))
    lectura = relationship("Lectura", back_populates="audios")
    
    # Relación con Fonema (opcional)
    fonema_id = Column(Integer, ForeignKey("fonemas.id"))
    fonema = relationship("Fonema", back_populates="audios")