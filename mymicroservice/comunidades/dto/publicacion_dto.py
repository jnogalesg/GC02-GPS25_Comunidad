from dataclasses import dataclass
from datetime import datetime

@dataclass
class PublicacionDTO:
    idPublicacion: str
    idComunidad: str
    titulo: str
    contenido: str
    rutaFichero: str | None  # puede ser nulo
    fecha: datetime
    meGusta: int 