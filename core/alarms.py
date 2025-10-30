class AlarmCenter:
    def __init__(self):
        self.alarms = []

    def raise_alarm(self, message):
        if message not in self.alarms:
            self.alarms.append(message)

    def get_alarms(self):
        return self.alarms