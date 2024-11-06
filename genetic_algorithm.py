""" Aquí se realiza la lógica para evaluar la mejor ruta en relación al algoritmo genético """
import random


class GeneticAlgorithm:
    """ Clase para ejecutar el algoritmo genético sobre una población de cromosomas. """

    def __init__(self, chromosomes, mutation_rate=0.1):
        """
        Inicializa la clase del algoritmo genético.

        Args:
            chromosomes (list): Población inicial de cromosomas (rutas).
            mutation_rate (float): Tasa de mutación para el algoritmo genético.
        """
        self.chromosomes = chromosomes
        self.mutation_rate = mutation_rate

    def fitness(self, chromosome):
        """
        Evalúa el fitness de un cromosoma en función de los factores como distancia, colisiones y giros.
        
        Args:
            chromosome (dict): Un cromosoma con ruta y métricas de evaluación.

        Returns:
            float: Valor de fitness, donde un valor mayor indica una mejor ruta.
        """
        # Fórmula de fitness, donde los mejores resultados tienen menos colisiones y distancia
        # Ajuste de pesos para cada parámetro en la fórmula de fitness
        weight_distance = 1.0
        weight_steps = 0.5
        weight_collisions = 2.0
        weight_turns = 1.5

        # Fitness inverso, penalizando colisiones y giros
        fitness_value = 1 / (
            (weight_distance * chromosome["distancia_recorrida"]) +
            (weight_steps * chromosome["cantidad_pasos"]) +
            (weight_collisions * chromosome["colisiones"]) +
            (weight_turns * chromosome["giros"] + 1)
        )

        return fitness_value
    
    def evaluate_population(self, result):
        """
        Evalúa todos los cromosomas de la población y actualiza sus métricas.

        Args:
            result (list): Lista de resultados obtenidos para cada cromosoma (distancia, colisiones, etc.).
        """
        for idx, chrom in enumerate(self.chromosomes):
            # Actualiza las métricas del cromosoma (este es un ejemplo, depende de cómo definas 'result')
            chrom["distancia_recorrida"] = result[idx]["distancia_recorrida"]
            chrom["cantidad_pasos"] = result[idx]["cantidad_pasos"]
            chrom["colisiones"] = result[idx]["colisiones"]
            chrom["giros"] = result[idx]["giros"]

    def get_best_chromosome(self):
        """
        Obtiene el mejor cromosoma basado en el fitness.

        Returns:
            dict: El cromosoma con el mejor fitness.
        """
        # Ordena la población según el valor de fitness
        best_chromosome = max(self.chromosomes, key=self.fitness)
        return best_chromosome

    def select_chromosomes(self):
        """
        Selecciona dos cromosomas con el mejor fitness para el crossover.
        
        Returns:
            tuple: Dos cromosomas seleccionados para la reproducción.
        """
        # Ordena la población de acuerdo al fitness
        sorted_chromosomes = sorted(
            self.chromosomes, key=lambda chrom: self.fitness(chrom), reverse=True)

        # Selección de los dos mejores
        return sorted_chromosomes[0], sorted_chromosomes[1]

    def crossover(self, parent1, parent2):
        """
        Realiza el crossover entre dos padres para generar un hijo.

        Args:
            parent1 (dict): Primer cromosoma padre.
            parent2 (dict): Segundo cromosoma padre.

        Returns:
            dict: Nuevo cromosoma hijo generado por el crossover.
        """
        # Punto de cruce aleatorio
        crossover_point = random.randint(1, len(parent1["ruta"]) - 1)

        # Creación de un nuevo cromosoma combinando las rutas de los padres
        child_route = parent1["ruta"][:crossover_point] + \
            parent2["ruta"][crossover_point:]

        # Creación del cromosoma hijo con valores iniciales de evaluación
        child_chromosome = {
            "ruta": child_route,
            "distancia_recorrida": 0,
            "cantidad_pasos": 0,
            "colisiones": 0,
            "giros": 0
        }

        return child_chromosome

    def mutate(self, chromosome):
        """
        Realiza una mutación en el cromosoma basado en la tasa de mutación.

        Args:
            chromosome (dict): Cromosoma a mutar.

        Returns:
            dict: Cromosoma con posibles cambios.
        """
        # Recorrer cada paso de la ruta para realizar mutaciones según la tasa de mutación
        for i in range(len(chromosome["ruta"])):
            if random.random() < self.mutation_rate:
                # Cambia el movimiento actual por uno aleatorio
                chromosome["ruta"][i] = random.choice([1, 2, 3, 4])

        return chromosome

    def genetic_algorithm(self, generations=100):
        """
        Ejecuta el ciclo completo del algoritmo genético para optimizar la población.

        Args:
            generations (int): Número de generaciones a ejecutar.

        Returns:
            list: Nueva población de cromosomas optimizada.
        """
        for generation in range(generations):
            new_population = []

            # Realizar selección, cruce y mutación para formar la nueva generación
            for _ in range(len(self.chromosomes) // 2):
                # Selección de los mejores padres
                parent1, parent2 = self.select_chromosomes()

                # Crossover entre los padres
                child1 = self.crossover(parent1, parent2)
                child2 = self.crossover(parent2, parent1)

                # Mutación de los hijos
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)

                # Agregar hijos a la nueva población
                new_population.extend([child1, child2])

            # Reemplazo de la población antigua con la nueva
            self.chromosomes = new_population

            # Reiniciar valores de evaluación para la nueva generación
            for chrom in self.chromosomes:
                chrom["distancia_recorrida"] = 0
                chrom["cantidad_pasos"] = 0
                chrom["colisiones"] = 0
                chrom["giros"] = 0

        return self.chromosomes
