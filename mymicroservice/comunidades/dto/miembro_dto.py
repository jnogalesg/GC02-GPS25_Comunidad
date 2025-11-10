from dataclasses import dataclass

@dataclass
class MiembroDTO:
    id: str
    nombreUsuario: str
    esArtista: bool
    rutaFoto: str | None = None # puede ser nulo