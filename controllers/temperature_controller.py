from models.temperature_model import TemperatureModel

class TemperatureController:
    def __init__(self, model: TemperatureModel):
        self.model = model

    def increase(self, room_name, value=1.0):
        self.model.increase_temp(room_name, value)

    def decrease(self, room_name, value=1.0):
        self.model.decrease_temp(room_name, value)

    def toggle(self, state: bool):
        self.model.toggle_thermostat(state)

    def get_state(self):
        return self.model.get_state()

    def check_anomalies(self):
        return self.model.check_anomalies()