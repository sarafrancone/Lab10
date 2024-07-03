from dataclasses import dataclass
@dataclass
class Contiguity:
    dyad: int
    state1no: int
    state1ab: str
    state2no: int
    state2ab: str
    year: int
    conttype: int
    version: float

    @property
    def get_state1no(self):
        return self.state1no

    @property
    def get_state2no(self):
        return self.state2no

    @property
    def get_state1ab(self):
        return self.state1ab

    @property
    def get_state2ab(self):
        return self.state2ab

    def __hash__(self):
        return hash(self.dyad)

    def __str__(self):
        return f"{self.state1ab} - {self.state2ab}"