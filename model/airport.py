from dataclasses import dataclass

@dataclass
class Airport:
    ID: int
    IATA_CODE: str
    AIRPORT: str
    CITY: str
    STATE: str
    COUNTRY: str
    LATITUDE: int
    LONGITUDE: int
    TIMEZONE_OFFSET: int

    def __hash__(self):
        return hash(self.ID)