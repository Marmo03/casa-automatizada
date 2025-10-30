from core.alarms import AlarmCenter
from core.interfaces import ISubsystem

class MasterController:
    def __init__(self, subsystems: list[ISubsystem]):
        self.subsystems = subsystems
        self.alarms = AlarmCenter()

    def check_all(self):
        # limpiamos alarmas viejas
        self.alarms = AlarmCenter()
        for s in self.subsystems:
            probs = s.check_anomalies()
            for p in probs:
                self.alarms.raise_alarm(p)

    def get_alarms(self):
        return self.alarms.get_alarms()