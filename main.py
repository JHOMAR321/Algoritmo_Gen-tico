""" Main execution file """
from robotv3 import Robot
from genetic_algorithm import GeneticAlgorithm
from chromosomev2 import Chromosome
from maze import Maze


class Main:
    """Clase principal para ejecutar el algoritmo genético en un robot que navega por un laberinto."""

    def __init__(self):
        pass

    def start_robot(self):
        """Inicializa el laberinto, crea los cromosomas y ejecuta el algoritmo genético para encontrar la mejor ruta."""

        # Configuración del laberinto
        maze_size = (5, 5)  # Tamaño del laberinto
        posicion_inicial_robot = (0, 0)
        posicion_goal_robot = (3, 3)
        num_chromosomes = 10  # Número de cromosomas en la población
        generations = 100  # Número de generaciones a ejecutar

        # Crear instancia del laberinto
        maze = Maze(*maze_size)
        maze.create_array_object(num_objects=5)
        maze.generate_matrix()

        # Crear cromosomas iniciales
        chromosome_creator = Chromosome(
            length_row=maze_size[0],
            length_column=maze_size[1],
            posicion_robot=posicion_inicial_robot,  # Cambiado aquí
            posicion_goal=posicion_goal_robot,  # Cambiado aquí
            num_chromosomes=num_chromosomes
        )
        chromosomes = chromosome_creator.generate_chromosomes()


        # Crear instancia del robot y algoritmo genético
        robot = Robot(maze.matrix, posicion_inicial_robot, posicion_goal_robot)
        algorithm = GeneticAlgorithm(chromosomes=chromosomes)

        # Ejecutar el algoritmo genético por varias generaciones
        for generation in range(generations):
            print(f"Generación {generation + 1}")

            # Asignar cromosomas al robot y obtener las métricas del recorrido
            robot.recibir_chromosomas(algorithm.chromosomes)
            result = robot.contar_rutas()  # Actualiza las métricas de cada cromosoma

            # Evaluar la población actual basada en las métricas obtenidas
            algorithm.evaluate_population(result)

            # Comprobar si ya se ha encontrado una solución óptima
            best_chromosome = algorithm.get_best_chromosome()
            if best_chromosome["distancia_recorrida"] == len(best_chromosome["ruta"]):
                print("¡Ruta óptima encontrada!")
                break

            # Generar una nueva población mediante selección, cruce y mutación
            new_population = []
            for _ in range(num_chromosomes // 2):
                # Selección de los mejores padres
                parent1, parent2 = algorithm.select_chromosomes()

                # Cruce entre los padres para generar dos hijos
                child1 = algorithm.crossover(parent1, parent2)
                child2 = algorithm.crossover(parent2, parent1)

                # Mutación de los hijos
                child1 = algorithm.mutate(child1)
                child2 = algorithm.mutate(child2)

                # Agregar hijos a la nueva población
                new_population.extend([child1, child2])

            # Reemplazar la población antigua con la nueva generación
            algorithm.chromosomes = new_population

            # Reiniciar métricas para la nueva generación
            for chrom in chromosomes:
                chrom["distancia_recorrida"] = 0
                chrom["cantidad_pasos"] = 0
                chrom["colisiones"] = 0
                chrom["giros"] = 0

            print(
                f"Mejor cromosoma de la generación {generation + 1}: {best_chromosome}")

        print("Algoritmo completado.")
        print("Mejor ruta encontrada:", best_chromosome)


if __name__ == "__main__":
    _robot = Main()
    _robot.start_robot()
