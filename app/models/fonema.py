from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Fonema(Base):
    __tablename__ = "fonemas"
    
    id = Column(Integer, primary_key=True, index=True)
    letra = Column(String(10), nullable=False)       # Ej: "A", "CH"
    ruta_audio = Column(String(255), nullable=False) # Ej: "/audios/fonema_a.mp3"
    
    # Relación con Audio (opcional)
    audios = relationship("Audio", back_populates="fonema")