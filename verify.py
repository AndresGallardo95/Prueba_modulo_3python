import preguntas as p

def verificar(alternativas, eleccion):
    # Devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c', 'd'].index(eleccion)

    # Generar lógica para determinar respuestas correctas
    ##########################################################################################
    # Se asume que la alternativa correcta es la que tiene el valor 1 en su lista
    correcta = False
    if alternativas[eleccion][1] == 1:
        print('Respuesta Correcta')
        correcta = True
    else:
        print('Respuesta Incorrecta')
        correcta = False
    ##########################################################################################
    
    return correcta

if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Ejemplo de uso: Siempre que se escoja la alternativa con alt_2 estará correcta (en este caso es alternativa B)
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    es_correcta = verificar(pregunta['alternativas'], respuesta)



