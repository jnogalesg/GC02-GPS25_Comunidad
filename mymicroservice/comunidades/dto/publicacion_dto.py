from dataclasses import dataclass
from datetime import datetime

@dataclass
class PublicacionDTO:
    id_publicacion: str
    id_comunidad: str
    titulo: str
    contenido: str
    rutaFichero: str | None  # puede ser nulo
    fecha: datetime
    meGusta: int | None  # puede ser nulo