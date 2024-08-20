preguntas_basicas = {
    'pregunta_1': {
        'enunciado': ['¿Cuál es el continente más grande por superficie?'],
        'alternativas': [
            ['África', 0], 
            ['América del Norte', 0], 
            ['Asia', 1], 
            ['Europa', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Cuál es el planeta más grande del sistema solar?'],
        'alternativas': [
            ['Tierra', 0], 
            ['Júpiter', 1], 
            ['Saturno', 0], 
            ['Neptuno', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Qué animal es conocido por ser el rey de la selva?'],
        'alternativas': [
            ['Leopardo', 0], 
            ['Elefante', 0], 
            ['León', 1], 
            ['Tigre', 0]
        ]
    },
    'pregunta_4': {
        'enunciado': ['¿Cuál es el elemento químico que tiene por símbolo H?'],
        'alternativas': [
            ['Helio', 0],
            ['Hidrógeno', 1],
            ['Hierro', 0],
            ['Hafnio', 0]
        ]
    },
    'pregunta_5': {
        'enunciado': ['¿Cuál es el país más poblado del mundo?'],
        'alternativas': [
            ['India', 0],
            ['Estados Unidos', 0],
            ['China', 1],
            ['Indonesia', 0]
        ]
    },
    'pregunta_6': {
        'enunciado': ['¿Cuál es el idioma más hablado en el mundo?'],
        'alternativas': [
            ['Inglés', 0],
            ['Español', 0],
            ['Mandarín', 1],
            ['Árabe', 0]
        ]
    }
}


preguntas_intermedias = {
    'pregunta_1': {
        'enunciado': ['¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?'],
        'alternativas': [
            ['1776', 1], 
            ['1789', 0], 
            ['1804', 0], 
            ['1812', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Cuál es el órgano más grande del cuerpo humano?'],
        'alternativas': [
            ['Corazón', 0], 
            ['Hígado', 0], 
            ['Piel', 1], 
            ['Pulmones', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Qué científico propuso la teoría de la evolución por selección natural?'],
        'alternativas': [
            ['Isaac Newton', 0], 
            ['Albert Einstein', 0], 
            ['Charles Darwin', 1], 
            ['Galileo Galilei', 0]
        ]
    },
    'pregunta_4': {
        'enunciado': ['¿Cuál es el río más caudaloso del mundo?'],
        'alternativas': [
            ['Nilo', 0],
            ['Yangtsé', 0],
            ['Amazonas', 1],
            ['Misisipi', 0]
        ]
    },
    'pregunta_5': {
        'enunciado': ['¿Qué país tiene la mayor cantidad de premios Nobel?'],
        'alternativas': [
            ['Reino Unido', 0],
            ['Alemania', 0],
            ['Estados Unidos', 1],
            ['Francia', 0]
        ]
    },
    'pregunta_6': {
        'enunciado': ['¿Qué estructura en el cerebro humano se asocia principalmente con la memoria?'],
        'alternativas': [
            ['Hipotálamo', 0],
            ['Cerebelo', 0],
            ['Hipocampo', 1],
            ['Corteza prefrontal', 0]
        ]
    }
}


preguntas_avanzadas = {
    'pregunta_1': {
        'enunciado': ['¿Cuál es el período de rotación del planeta Mercurio alrededor del Sol?'],
        'alternativas': [
            ['88 días', 1], 
            ['365 días', 0], 
            ['225 días', 0], 
            ['687 días', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Cuál es el nombre del primer satélite artificial lanzado al espacio?'],
        'alternativas': [
            ['Voyager 1', 0], 
            ['Luna 2', 0], 
            ['Sputnik 1', 1], 
            ['Explorer 1', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿En qué país se originó la peste negra que devastó Europa en el siglo XIV?'],
        'alternativas': [
            ['Italia', 0], 
            ['Francia', 0], 
            ['China', 1], 
            ['España', 0]
        ]
    },
    'pregunta_4': {
        'enunciado': ['¿Cuál es la velocidad de la luz en el vacío?'],
        'alternativas': [
            ['300,000 km/s', 1],
            ['150,000 km/s', 0],
            ['500,000 km/s', 0],
            ['750,000 km/s', 0]
        ]
    },
    'pregunta_5': {
        'enunciado': ['¿Qué filósofo escribió "La república"?'],
        'alternativas': [
            ['Aristóteles', 0],
            ['Platón', 1],
            ['Sócrates', 0],
            ['Demócrito', 0]
        ]
    },
    'pregunta_6': {
        'enunciado': ['¿Cuál es el país más joven del mundo en términos de independencia?'],
        'alternativas': [
            ['Kosovo', 0],
            ['Timor Oriental', 0],
            ['Sudán del Sur', 1],
            ['Montenegro', 0]
        ]
    }
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}