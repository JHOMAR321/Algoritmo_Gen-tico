from robotv3 import Robot


# Crear una matriz de ejemplo (0: libre, 1: obstáculo)
matrix = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

# Posiciones inicial y objetivo
posicion_inicial_robot = (0, 0)
posicion_goal_robot = (3, 3)

# Crear instancias de las clases y ejecutar
robot = Robot(matrix, posicion_inicial_robot, posicion_goal_robot)
chromosomes = [
    {"ruta": [2, 4, 3, 2, 4, 2, 3, 2, 2, 1], "distancia_recorrida": 0,
        "cantidad_pasos": 0, "colisiones": 0, "giros": 0},
    # Añadir más cromosomas si es necesario
]

# Asignar cromosomas al robot y contar rutas
robot.recibir_chromosomas(chromosomes)
result = robot.contar_rutas()

# Mostrar resultados
print(result)
