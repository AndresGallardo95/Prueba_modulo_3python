def print_pregunta(enunciado, alternativas):
    # Imprimir el enunciado de la pregunta
    ###############################################################
    if isinstance(enunciado, list):
        print(enunciado[0])
    else:
        print(enunciado)

    print()  # Salto de línea después del enunciado

    # Definir las letras asociadas a las alternativas
    letras = ['A', 'B', 'C', 'D']

    # Imprimir cada alternativa con su letra asociada
    for i, alternativa in enumerate(alternativas):
        print(f"{letras[i]}. {alternativa[0]}")
    ###############################################################

if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    import preguntas as p
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
