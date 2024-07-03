from dataclasses import dataclass
@dataclass
class Country:
    StateAbb: str
    CCode: int
    StateNme: str

    @property
    def get_stateAbb(self):
        return self.StateAbb

    @property
    def get_ccode(self):
        return self.CCode

    @property
    def get_stateNme(self):
        return self.StateNme

    def __hash__(self):
        return hash(self.CCode)

    def __str__(self):
        return f"{self.StateNme}"