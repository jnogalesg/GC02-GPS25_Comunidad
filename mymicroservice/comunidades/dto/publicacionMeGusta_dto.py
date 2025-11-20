from dataclasses import dataclass
from datetime import datetime

@dataclass
class PublicacionMeGustaDTO:
    idPublicacion: int
    idUsuario: int
    fechaMeGusta: datetime