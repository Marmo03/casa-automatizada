from models.waste_model import WasteModel

class WasteController:
    def __init__(self, model: WasteModel):
        self.model = model

    def add_recyclable(self, amount):
        self.model.add_recyclable(amount)

    def add_non_recyclable(self, amount):
        self.model.add_non_recyclable(amount)

    def evacuate(self):
        self.model.evacuate()

    def get_state(self):
        return self.model.get_state()

    def check_anomalies(self):
        return self.model.check_anomalies()