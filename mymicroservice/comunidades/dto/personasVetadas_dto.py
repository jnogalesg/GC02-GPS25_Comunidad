from dataclasses import dataclass
from datetime import datetime

@dataclass
class PersonaVetadaDTO:
    idMiembro: str
    idComunidad: str
    fechaVeto: datetime