from models.access_model import AccessModel

class AccessController:
    def __init__(self, model: AccessModel):
        self.model = model

    def login(self, user, pwd):
        return self.model.login(user, pwd)

    def logout(self):
        self.model.logout()

    def add_visitor(self, name):
        self.model.add_visitor(name)

    def admit_visitor(self):
        return self.model.admit_visitor()

    def reset_alarm(self):
        self.model.reset_alarm()

    def get_state(self):
        return self.model.get_state()

    def check_anomalies(self):
        return self.model.check_anomalies()