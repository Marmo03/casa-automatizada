from core.interfaces import ISubsystem
from core.batteries import BatteryPack

class WasteModel(ISubsystem):
    def __init__(self):
        self.recyclable = 0.0
        self.non_recyclable = 0.0
        self.limit = 30.0  # si supera esto, alarma
        self.batteries = BatteryPack()

    def add_recyclable(self, amount):
        self.recyclable += amount

    def add_non_recyclable(self, amount):
        self.non_recyclable += amount

    def evacuate(self):
        self.recyclable = 0.0
        self.non_recyclable = 0.0

    def get_state(self):
        return {
            "recyclable": self.recyclable,
            "non_recyclable": self.non_recyclable,
            "limit": self.limit,
            "batteries": self.batteries.get_levels()
        }

    def check_anomalies(self):
        problems = []
        if not self.batteries.has_minimum():
            problems.append("Residuos: no hay batería al 100%.")
        total = self.recyclable + self.non_recyclable
        if total > self.limit:
            problems.append("Residuos: exceso de residuos sin evacuar.")
        return problems