from app.database import engine, SessionLocal
from sqlalchemy import text  # <-- Añade esta importación

def test_connection():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))  # <-- Envuelve el SQL con text()
        print("✅ Conexión exitosa a la DB")
    except Exception as e:
        print("❌ Error de conexión:", e)
    finally:
        db.close()

test_connection()