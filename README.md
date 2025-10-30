# Sistema de Control Domótico

Un sistema de control maestro para la automatización de viviendas implementado en Python siguiendo principios SOLID y patrones de diseño MVC.

## 📋 Características

### Subsistemas Implementados

- **🔐 Control de Acceso**: Gestión de usuarios, visitantes, intentos fallidos y alarmas de seguridad
- **💡 Control de Luces**: Administración de iluminación por habitaciones con detección de fallos
- **🌡️ Control de Temperatura**: Monitoreo y control térmico con termostato inteligente
- **🗑️ Control de Residuos**: Gestión de residuos reciclables y no reciclables con alertas

### Control Maestro

- **🎯 Interfaz Unificada**: Acceso centralizado a todos los subsistemas
- **🔋 Monitoreo de Baterías**: Cada subsistema cuenta con 3 baterías (mínimo una al 100%)
- **🚨 Sistema de Alarmas**: Detección automática de anomalías y alertas centralizadas
- **📊 Verificación de Estado**: Monitoreo continuo del estado de la vivienda

## 🏗️ Arquitectura

### Patrón MVC (Model-View-Controller)

```
📁 models/          # Lógica de negocio y datos
📁 views/           # Interfaz de usuario
📁 controllers/     # Coordinación entre modelos y vistas
📁 core/            # Componentes centrales (interfaces, alarmas, baterías)
```

### Principios SOLID Aplicados

- **SRP**: Cada clase tiene una responsabilidad específica
- **OCP**: Extensible mediante interfaces
- **LSP**: Implementación correcta de `ISubsystem`
- **ISP**: Interfaces específicas y cohesivas
- **DIP**: Dependencia de abstracciones, no de concreciones

## 🚀 Instalación y Uso

### Requisitos
- Python 3.8 o superior

### Ejecución
```bash
python main.py
```

### Estructura de Archivos
```
sistema-domotico/
├── main.py                 # Punto de entrada principal
├── controllers/
│   ├── access_controller.py
│   ├── lighting_controller.py
│   ├── temperature_controller.py
│   ├── waste_controller.py
│   └── master_controller.py
├── models/
│   ├── access_model.py
│   ├── lighting_model.py
│   ├── temperature_model.py
│   └── waste_model.py
├── views/
│   └── console_view.py
└── core/
    ├── interfaces.py        # Interfaz ISubsystem
    ├── alarms.py           # Sistema de alarmas
    └── batteries.py        # Gestión de baterías
```

## 🎮 Simulación

El sistema incluye una simulación completa que demuestra:

1. **Intentos de acceso fallidos** → Activación de alarma de seguridad
2. **Control de iluminación** → Encendido de luces y simulación de fallos
3. **Gestión térmica** → Modificación de temperatura fuera de rango
4. **Control de residuos** → Acumulación excesiva de desechos

## 📊 Ejemplo de Salida

```
========== ESTADO DE LA CASA ==========

[ACCESO]
Personas dentro: 0
En espera: 0
Intentos fallidos: 3
Alarma acceso: True
Baterías: [100.0, 80.0, 70.0]

[LUCES]
- Sala: ON | fallo=False
- Cocina: OFF | fallo=True
- Habitación 1: OFF | fallo=False
Baterías: [100.0, 80.0, 70.0]

[TEMPERATURA]
Rango permitido: 18.0 - 28.0
- Sala: 28.0°C
- Cocina: 22.0°C
- Habitación 1: 22.0°C
Termostato: ON
Baterías: [100.0, 80.0, 70.0]

[RESIDUOS]
Reciclables: 15.0
No reciclables: 20.0
Límite: 30.0
Baterías: [100.0, 80.0, 70.0]

[ALARMAS]
 - Acceso: demasiados intentos fallidos.
 - Luces: luminaria con fallo en Cocina.
 - Residuos: exceso de residuos sin evacuar.
=======================================
```

## 🛠️ Patrones de Diseño Implementados

- **Strategy Pattern**: Diferentes estrategias para cada subsistema
- **Observer Pattern**: Control maestro observa todos los subsistemas
- **Facade Pattern**: `MasterController` como fachada del sistema
- **Factory Pattern**: Creación organizada de componentes

## 📝 Licencia

Este proyecto fue desarrollado como parte de un ejercicio académico enfocado en la aplicación de principios de ingeniería de software.

## 👨‍💻 Autor

Desarrollado aplicando principios SOLID y patrones de diseño para crear un sistema robusto, mantenible y escalable.