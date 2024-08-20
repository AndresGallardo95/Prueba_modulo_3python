# APP ADL desarrolladores // Fundamentos de programación en Python

ADL Desarrolladores es una entidad dedicada a desarrollar apps entretenidas.
Se desarrolla una App en Python que permite jugar una trivia interactiva. Esta App tendrá preguntas con 3 niveles de dificultad:

● Básica
● Intermedia
● Avanzada

El jugador define el número de preguntas a responder correspondientes a cada nivel de dificultad, y gana al responder todas las preguntas correctamente. Las preguntas deben aparecer en un orden aleatorio, y además cada vez que alguien ejecute la app las alternativas deben ser cambiadas de orden para evitar que alguien encuentre algún patrón de resolución.

Ya que el programa es complejo se ha generado un backlog con tareas muy específicas, las cuales son desarrolladas paso a paso antes de ensamblar la app final.
Todas las subtareas consistirán en la creación de un script en Python, la que contendrá las especificaciones de una funcionalidad.

# Trivia en Python

## Descripción General

Este proyecto es una aplicación de trivia en línea de comandos escrita en Python. El programa permite a los usuarios responder preguntas de diferentes niveles de dificultad y validar sus respuestas. La aplicación incluye múltiples módulos para gestionar la selección de preguntas, validar respuestas, mostrar preguntas con formato, y manejar la lógica del juego.

## Estructura del Proyecto

El proyecto se compone de varios archivos Python que se integran para crear la experiencia de trivia:

- `main.py`: Controla el flujo principal del juego.
- `preguntas.py`: Contiene los bancos de preguntas y alternativas organizadas por nivel de dificultad.
- `verify.py`: Verifica si la respuesta del usuario es correcta.
- `question.py`: Selecciona preguntas aleatorias según el nivel de dificultad.
- `print_preguntas.py`: Muestra el enunciado y las alternativas en un formato específico.
- `level.py`: Determina el nivel de dificultad de las preguntas basándose en el número de pregunta y las opciones seleccionadas por el usuario.

## Instalación

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/trivia-python.git
#
