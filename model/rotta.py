from dataclasses import dataclass
from model.airport import Airport

@dataclass
class Rotta:
    a1: Airport
    a2: Airport
    totDistanza: int
    nVoli: int

    def __post_init__(self):
        self.peso = float(self.totDistanza / self.nVoli)






