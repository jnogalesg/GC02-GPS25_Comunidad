from dataclasses import dataclass
from datetime import datetime

@dataclass
class ComunidadDTO:
    id: str
    id_artista_creador: str
    nombre_comunidad: str
    desc_comunidad: str | None # puede ser nulo
    ruta_imagen: str | None # puede ser nulo
    fecha_creacion: datetime
    palabras_vetadas: str | None # puede ser nulo