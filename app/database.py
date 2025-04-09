from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://aprenderleer:pezcadofrito.1@localhost/aprenderleer_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    echo=True  # Opcional: muestra logs SQL en consola
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para todos los modelos (¡Solo debe declararse una vez!)
Base = declarative_base()

# Importa TODOS los modelos aquí (asegura que se registren en Base.metadata)
from app.models.lectura import Lectura
from app.models.audio import Audio
from app.models.fonema import Fonema

# Función para inyección de dependencias (añadir esto al final)
def get_db():
    """
    Generador de sesiones para dependencias.
    Uso:
    db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()