# Interfaz que deben implementar todos los subsistemas

from abc import ABC, abstractmethod

class ISubsystem(ABC):
    @abstractmethod
    def get_state(self):
        """Debe devolver un dict con el estado para mostrar."""
        pass

    @abstractmethod
    def check_anomalies(self):
        """Debe devolver una lista de strings con problemas."""
        pass