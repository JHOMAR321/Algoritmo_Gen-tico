""" Aquí se crea los cromosomas (rutas) de manera aleatoria """
import random

class Chromosome:
    """ Clase para representar un cromosoma que contiene una ruta para el robot. """
    
    def __init__(self, length_row, length_column, posicion_robot, posicion_goal, num_chromosomes=10):
        """
        Inicializa los parámetros para el cromosoma.

        Args:
            length_row (int): Número de filas en la matriz.
            length_column (int): Número de columnas en la matriz.
            posicion_robot (tuple): Posición inicial del robot (fila, columna).
            posicion_goal (tuple): Posición objetivo o meta (fila, columna).
            num_chromosomes (int): Número de cromosomas (rutas) a generar.
        """
        print(
            f"Inicializando Chromosome: {length_row}, {length_column}, {posicion_robot}, {posicion_goal}, {num_chromosomes}")
        self.length_row = length_row
        self.length_column = length_column
        self.posicion_robot = posicion_robot
        self.posicion_goal = posicion_goal
        self.num_chromosomes = num_chromosomes
        
    def calculate_chromosome_length(self):
        """
        Calcula una longitud aproximada para los cromosomas basada en la distancia de Manhattan 
        entre el inicio y la meta, con algunos pasos adicionales para explorar.
        
        Returns:
            int: Longitud estimada del cromosoma.
        """
        # Distancia de Manhattan entre la posición inicial y la meta
        distance = abs(self.posicion_robot[0] - self.posicion_goal[0]) + abs(self.posicion_robot[1] - self.posicion_goal[1])
        # Añadimos algunos pasos adicionales para dar flexibilidad en la ruta
        return distance + random.randint(2, 5)

    def generate_chromosome(self):
        """
        Genera un cromosoma aleatorio, que es una lista de movimientos.

        Returns:
            dict: Un cromosoma representado como un diccionario con la ruta y valores adicionales para evaluación.
        """
        chromosome_length = self.calculate_chromosome_length()
        # Crear un cromosoma como una secuencia de movimientos aleatorios
        chromosome = {
            # La secuencia de movimientos
            "ruta": [random.choice([1, 2, 3, 4]) for _ in range(chromosome_length)],
            "distancia_recorrida": 0,
            "cantidad_pasos": 0,
            "colisiones": 0,
            "giros": 0
        }
        return chromosome

    def generate_chromosomes(self):
        """
        Genera una población de cromosomas aleatorios.

        Returns:
            list: Lista de cromosomas, donde cada cromosoma es un diccionario con la ruta y métricas de evaluación.
        """
        chromosomes = [self.generate_chromosome()
                       for _ in range(self.num_chromosomes)]
        return chromosomes

    def update_chromosome_metrics(self, chromosome, distancia_recorrida, cantidad_pasos, colisiones, giros):
        """
        Actualiza un cromosoma con los valores de evaluación.

        Args:
            chromosome (dict): Cromosoma a actualizar.
            distancia_recorrida (int): Distancia total recorrida en la ruta.
            cantidad_pasos (int): Número total de pasos en la ruta.
            colisiones (int): Número de colisiones encontradas en la ruta.
            giros (int): Número de giros realizados en la ruta.
        """
        chromosome["distancia_recorrida"] = distancia_recorrida
        chromosome["cantidad_pasos"] = cantidad_pasos
        chromosome["colisiones"] = colisiones
        chromosome["giros"] = giros
