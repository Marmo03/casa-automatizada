from core.interfaces import ISubsystem
from core.batteries import BatteryPack

class TempRoom:
    def __init__(self, name, temp=22.0):
        self.name = name
        self.temp = temp


class TemperatureModel(ISubsystem):
    def __init__(self):
        self.rooms = [
            TempRoom("Sala"),
            TempRoom("Cocina"),
            TempRoom("Habitación 1"),
        ]
        self.min_temp = 18.0
        self.max_temp = 28.0
        self.thermostat_on = True
        self.batteries = BatteryPack()

    def increase_temp(self, room_name, value=1.0):
        for r in self.rooms:
            if r.name == room_name:
                r.temp = min(r.temp + value, self.max_temp)

    def decrease_temp(self, room_name, value=1.0):
        for r in self.rooms:
            if r.name == room_name:
                r.temp = max(r.temp - value, self.min_temp)

    def toggle_thermostat(self, state):
        self.thermostat_on = state

    def get_state(self):
        rooms_data = []
        for r in self.rooms:
            rooms_data.append({
                "name": r.name,
                "temp": r.temp
            })
        return {
            "rooms": rooms_data,
            "min": self.min_temp,
            "max": self.max_temp,
            "thermostat_on": self.thermostat_on,
            "batteries": self.batteries.get_levels()
        }

    def check_anomalies(self):
        problems = []
        if not self.batteries.has_minimum():
            problems.append("Temperatura: no hay batería al 100%.")
        for r in self.rooms:
            if r.temp < self.min_temp or r.temp > self.max_temp:
                problems.append(f"Temperatura: {r.name} fuera de rango ({r.temp}°C).")
        return problems