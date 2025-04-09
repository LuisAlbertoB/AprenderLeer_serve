# Importa explícitamente todos los modelos
from .lectura import Lectura
from .audio import Audio
from .fonema import Fonema

# Lista explícita para ayudar a herramientas como Alembic
__all__ = ['Lectura', 'Audio', 'Fonema']