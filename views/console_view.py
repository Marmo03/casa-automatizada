# views/console_view.py

class ConsoleView:
    @staticmethod
    def show(access_state, lights_state, temp_state, waste_state, alarms):
        print("========== ESTADO DE LA CASA ==========")

        print("\n[ACCESO]")
        print("Personas dentro:", access_state["people_inside"])
        print("En espera:", access_state["waiting"])
        print("Intentos fallidos:", access_state["failed_attempts"])
        print("Alarma acceso:", access_state["alarm"])
        print("Baterías:", access_state["batteries"])

        print("\n[LUCES]")
        for r in lights_state["rooms"]:
            print(f"- {r['name']}: {'ON' if r['on'] else 'OFF'} | fallo={r['fail']}")
        print("Baterías:", lights_state["batteries"])

        print("\n[TEMPERATURA]")
        print("Rango permitido:", temp_state["min"], "-", temp_state["max"])
        for r in temp_state["rooms"]:
            print(f"- {r['name']}: {r['temp']}°C")
        print("Termostato:", "ON" if temp_state["thermostat_on"] else "OFF")
        print("Baterías:", temp_state["batteries"])

        print("\n[RESIDUOS]")
        print("Reciclables:", waste_state["recyclable"])
        print("No reciclables:", waste_state["non_recyclable"])
        print("Límite:", waste_state["limit"])
        print("Baterías:", waste_state["batteries"])

        print("\n[ALARMAS]")
        if alarms:
            for a in alarms:
                print(" -", a)
        else:
            print("Sin alarmas.")
        print("=======================================")