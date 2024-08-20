# No modificar
from verify import verificar
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
import time
import os
import sys

# valores iniciales
n_pregunta = 0
continuar = 'y'
correcto = True
p_level = 10
op_sys = 'cls' if sys.platform == 'win32' else 'clear'

# ----------------------------------------

os.system(op_sys)  # limpiar pantalla

print('Bienvenido a la Trivia')
opcion = input('''Ingrese una opción para Jugar!
        1. Jugar
        0. Salir
        
    > ''')

# 1. Validar opción
opcion = opcion.strip()  # Quitar espacios en blanco adicionales
if opcion not in ['0', '1']:
    print('Opción inválida. Por favor, elija 0 o 1.')
    exit()

# 2. Definir el comportamiento de Salir
if opcion == '0':
    print('Nos vemos pronto!')
    time.sleep(2)
    os.system(op_sys)
    exit()

# Funcionamiento de preguntas
while correcto and n_pregunta < 3 * p_level:

    if n_pregunta == 0:
        p_level = input('¿Cuántas preguntas por nivel? (Máximo 3): ')
        # 3. Validar el número de preguntas por nivel
        if not p_level.isdigit() or int(p_level) not in [1, 2, 3]:
            print('Número de preguntas por nivel inválido. Debe ser 1, 2 o 3.')
            exit()
        p_level = int(p_level)

    if continuar == 'y':
        # Contador de preguntas
        n_pregunta += 1

        # 4. Escoger el nivel de la pregunta
        nivel = choose_level(n_pregunta, p_level)

        print(f'Pregunta {n_pregunta}:')

        # 5. Escoger el enunciado y las alternativas de una pregunta según el nivel escogido
        enunciado, alternativas = choose_q(nivel)

        # 6. Imprimir el enunciado y sus alternativas en pantalla
        print_pregunta(enunciado, alternativas)

        respuesta = input('Escoja la alternativa correcta:\n> ').lower()

        # 7. Validar la respuesta entregada
        if respuesta not in ['a', 'b', 'c', 'd']:
            print('Opción inválida. Debe ser una de las opciones: a, b, c, o d.')
            exit()

        # 8. Verificar si la respuesta es correcta o no
        correcto = verificar(alternativas, respuesta)

        if correcto and n_pregunta < 3 * p_level:
            print('¡Muy bien, sigue así!')
            continuar = input('¿Desea continuar? [y/n]: ').lower()

            # 9. Validar si es que se responde y o n
            if continuar not in ['y', 'n']:
                print('Opción inválida. Por favor, elija y o n.')
                exit()

            os.system(op_sys)

        elif correcto and n_pregunta == 3 * p_level:
            print(f'¡Felicitaciones, has respondido {3 * p_level} preguntas correctas! \nHas ganado la Trivia \n¡Gracias por jugar, hasta luego!')
            time.sleep(3)
            os.system(op_sys)
            exit()

        else:
            print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas.\n¡Sigue participando!')
            time.sleep(3)
            exit()

    else:
        print('Nos vemos la próxima vez, sigue practicando.')
        time.sleep(3)
        exit()
