from core.interfaces import ISubsystem
from core.batteries import BatteryPack

class AccessModel(ISubsystem):
    def __init__(self):
        # usuarios quemados para la simulación
        self.users = {
            "juan": "1234",
            "admin": "admin"
        }
        self.people_inside = 0
        self.waiting_list = []
        self.failed_attempts = 0
        self.alarm_on = False
        self.batteries = BatteryPack()

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            self.people_inside += 1
            return True
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                self.alarm_on = True
            return False

    def logout(self):
        if self.people_inside > 0:
            self.people_inside -= 1

    def add_visitor(self, visitor_name):
        self.waiting_list.append(visitor_name)

    def admit_visitor(self):
        if self.waiting_list:
            name = self.waiting_list.pop(0)
            self.people_inside += 1
            return name
        return None

    def reset_alarm(self):
        self.alarm_on = False
        self.failed_attempts = 0

    # --- interfaz ---
    def get_state(self):
        return {
            "people_inside": self.people_inside,
            "waiting": len(self.waiting_list),
            "failed_attempts": self.failed_attempts,
            "alarm": self.alarm_on,
            "batteries": self.batteries.get_levels()
        }

    def check_anomalies(self):
        problems = []
        if not self.batteries.has_minimum():
            problems.append("Acceso: no hay batería al 100%.")
        if self.alarm_on:
            problems.append("Acceso: demasiados intentos fallidos.")
        return problems