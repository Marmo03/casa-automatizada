# main.py

from models.access_model import AccessModel
from models.lighting_model import LightingModel
from models.temperature_model import TemperatureModel
from models.waste_model import WasteModel

from controllers.access_controller import AccessController
from controllers.lighting_controller import LightingController
from controllers.temperature_controller import TemperatureController
from controllers.waste_controller import WasteController
from controllers.master_controller import MasterController

from views.console_view import ConsoleView


def main():
    # MODELOS
    access_m = AccessModel()
    lights_m = LightingModel()
    temp_m = TemperatureModel()
    waste_m = WasteModel()

    # CONTROLADORES
    access_c = AccessController(access_m)
    lights_c = LightingController(lights_m)
    temp_c = TemperatureController(temp_m)
    waste_c = WasteController(waste_m)

    # CONTROL MAESTRO (recibe los modelos porque implementan ISubsystem)
    master = MasterController([
        access_m,
        lights_m,
        temp_m,
        waste_m
    ])

    # ====== SIMULACIÓN ======
    # 1. acceso con 3 fallos
    access_c.login("intruso", "000")
    access_c.login("intruso", "000")
    access_c.login("intruso", "000")  # aquí ya debe encender alarma acceso

    # 2. luces: encender sala y dañar cocina
    lights_c.turn_on_room("Sala")
    lights_c.set_failure("Cocina", 0)

    # 3. temperatura: pasar sala del rango
    temp_c.increase("Sala", 10)

    # 4. residuos: meter basura hasta pasarse
    waste_c.add_recyclable(15)
    waste_c.add_non_recyclable(20)

    # revisar todo
    master.check_all()

    # mostrar
    ConsoleView.show(
        access_c.get_state(),
        lights_c.get_state(),
        temp_c.get_state(),
        waste_c.get_state(),
        master.get_alarms()
    )


if __name__ == "__main__":
    main()