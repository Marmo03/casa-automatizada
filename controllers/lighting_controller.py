# controllers/lighting_controller.py

from models.lighting_model import LightingModel

class LightingController:
    def __init__(self, model: LightingModel):
        self.model = model

    def turn_on_room(self, room_name):
        for r in self.model.rooms:
            if r.name == room_name:
                r.turn_on_all()

    def turn_off_room(self, room_name):
        for r in self.model.rooms:
            if r.name == room_name:
                r.turn_off_all()

    def set_failure(self, room_name, index):
        for r in self.model.rooms:
            if r.name == room_name:
                r.set_failure(index)

    def get_state(self):
        return self.model.get_state()

    def check_anomalies(self):
        return self.model.check_anomalies()