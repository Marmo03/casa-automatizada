from core.interfaces import ISubsystem
from core.batteries import BatteryPack

class RoomLights:
    def __init__(self, name, num_lights):
        self.name = name
        # False = apagada
        self.lights_state = [False] * num_lights
        # True = funciona
        self.lights_ok = [True] * num_lights

    def turn_on_all(self):
        self.lights_state = [True] * len(self.lights_state)

    def turn_off_all(self):
        self.lights_state = [False] * len(self.lights_state)

    def set_failure(self, index):
        if 0 <= index < len(self.lights_ok):
            self.lights_ok[index] = False

    def has_failure(self):
        return not all(self.lights_ok)

    def is_any_on(self):
        return any(self.lights_state)


class LightingModel(ISubsystem):
    def __init__(self):
        # puedes cambiar la casa aquí
        self.rooms = [
            RoomLights("Sala", 2),
            RoomLights("Cocina", 1),
            RoomLights("Habitación 1", 2),
        ]
        self.batteries = BatteryPack()

    def get_state(self):
        rooms_data = []
        for r in self.rooms:
            rooms_data.append({
                "name": r.name,
                "on": r.is_any_on(),
                "fail": r.has_failure()
            })
        return {
            "rooms": rooms_data,
            "batteries": self.batteries.get_levels()
        }

    def check_anomalies(self):
        problems = []
        if not self.batteries.has_minimum():
            problems.append("Luces: no hay batería al 100%.")
        for r in self.rooms:
            if r.has_failure():
                problems.append(f"Luces: luminaria con fallo en {r.name}.")
        return problems