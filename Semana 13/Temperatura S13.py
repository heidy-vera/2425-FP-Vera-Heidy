#Definicion de Funciones
temperaturas = [
    [   # Tena
        [   # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 21}
        ]
    ],
    [   # Pichincha
        [
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 29}
        ],
        [
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 36},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 31}
        ],
        [
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 30}
        ],
        [
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    [   # Machala
        [
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 32}
        ],
        [
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 31}
        ],
        [
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 23}
        ],
        [
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 20}
        ]
    ]
]
# Lista de nombres de ciudades
ciudades = ["Tena", "Pichincha", "Machala"]

# Función para calcular el promedio de temperatura por ciudad
def temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de un conjunto de ciudades.

    Args:
        temperaturas (list): Lista de ciudades con sus temperaturas semanales.

    Returns:
        dict: Diccionario con nombres de ciudades como claves y su temperatura promedio.
    """
    temperaturas_promedio = {}

    for ciudad_idx, ciudad in enumerate(temperaturas):
        total_temp = 0
        total_dias = 0

        for semana in ciudad:
            for dia in semana:
                total_temp += dia["temp"]
                total_dias += 1

        promedio_ciudad = total_temp / total_dias
        temperaturas_promedio[ciudades[ciudad_idx]] = round(promedio_ciudad, 2)

    return temperaturas_promedio

# Llamamos a la función para calcular las temperaturas promedio
resultados = temperatura_promedio(temperaturas)

# Mostramos los resultados
print("\nTemperaturas Promedio por Ciudad:")
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio:.2f}°C")
