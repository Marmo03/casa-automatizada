# Manejito de las 3 baterías

class BatteryPack:
    def __init__(self):
        # 3 baterías por requisito
        self.batteries = [100.0, 80.0, 70.0]

    def has_minimum(self):
        """True si al menos una está al 100%."""
        for b in self.batteries:
            if b == 100.0:
                return True
        return False

    def get_levels(self):
        return self.batteries