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
        self.selection_population = []
        self.crossover_population = []
        self.mutated_population = []
        self.fitness_scores = []

    def fitness(self, chromosome):
        """
        Evalúa el fitness de un cromosoma en función de los factores como distancia, colisiones y giros.
        
        Args:
            chromosome (dict): Un cromosoma con ruta y métricas de evaluación.

        Returns:
            float: Valor de fitness, donde un valor mayor indica una mejor ruta.
        """
        weight_distance = 1.0
        weight_steps = 0.5
        weight_collisions = 2.0
        weight_turns = 1.5

        try:
            fitness_value = 1 / (
                (weight_distance * chromosome["distancia_recorrida"]) +
                (weight_steps * chromosome["cantidad_pasos"]) +
                (weight_collisions * chromosome["colisiones"]) +
                (weight_turns * chromosome["giros"] + 1)
            )
        except ZeroDivisionError:
            fitness_value = 0

        return fitness_value

    def evaluate_population(self, result):
        """
        Evalúa todos los cromosomas de la población y actualiza sus métricas.

        Args:
            result (list): Lista de resultados obtenidos para cada cromosoma (distancia, colisiones, etc.).
        """
        for idx, chrom in enumerate(self.chromosomes):
            chrom["distancia_recorrida"] = result[idx]["distancia_recorrida"]
            chrom["cantidad_pasos"] = result[idx]["cantidad_pasos"]
            chrom["colisiones"] = result[idx]["colisiones"]
            chrom["giros"] = result[idx]["giros"]

    def select_chromosomes(self):
        """
        Selecciona los dos cromosomas con el mayor fitness para el crossover.
        
        Returns:
            tuple: Dos cromosomas seleccionados para la reproducción.
        """
        sorted_chromosomes = sorted(
            self.chromosomes, key=lambda chrom: self.fitness(chrom), reverse=True
        )
        # Guardar los dos cromosomas seleccionados
        self.selection_population = [sorted_chromosomes[0], sorted_chromosomes[1]]
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
        crossover_point = random.randint(1, len(parent1["ruta"]) - 1)
        child_route = parent1["ruta"][:crossover_point] + parent2["ruta"][crossover_point:]

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
        for i in range(len(chromosome["ruta"])):
            if random.random() < self.mutation_rate:
                chromosome["ruta"][i] = random.choice([1, 2, 3, 4])

        return chromosome

    def genetic_algorithm(self, generations=1):
        """
        Ejecuta el ciclo completo del algoritmo genético para optimizar la población.

        Args:
            generations (int): Número de generaciones a ejecutar.

        Returns:
            list: Nueva población de cromosomas optimizada.
        """
        for generation in range(generations):
            new_population = []

            # Selección de los mejores padres
            parent1, parent2 = self.select_chromosomes()

            # Generar dos hijos a partir del crossover y aplicarles mutación
            child1 = self.mutate(self.crossover(parent1, parent2))
            child2 = self.mutate(self.crossover(parent2, parent1))

            # Repetimos el proceso para obtener 4 cromosomas en total
            child3 = self.mutate(self.crossover(parent1, parent2))
            child4 = self.mutate(self.crossover(parent2, parent1))

            # Añadir los hijos generados a la nueva población
            new_population.extend([child1, child2, child3, child4])

            # Guardar las poblaciones de crossover y mutación para visualización
            self.crossover_population = [child1, child2, child3, child4]
            self.mutated_population = new_population

            # Reemplazo de la población antigua con la nueva
            self.chromosomes = new_population

        return self.chromosomes

    def mostrar_tabla(self):
        """Muestra una tabla con los resultados de cada cromosoma ordenados por fitness."""
        print("\nTabla de Resultados:")
        print(f"{'Cromosomas':<30}{'Fitness':<20}{'Selección':<30}{'Crossover':<30}{'Mutación':<30}")
        print("=" * 135)

        # Ordenar la población actual por fitness de mayor a menor
        sorted_chromosomes = sorted(self.chromosomes, key=lambda chrom: self.fitness(chrom), reverse=True)

        # Mostrar todos los cromosomas con sus detalles de selección, crossover y mutación
        for i, chrom in enumerate(sorted_chromosomes):
            cromosomas = str(chrom["ruta"])
            fitness = f"{self.fitness(chrom):.2f}"
            seleccion = str(self.selection_population[i]["ruta"]) if i < len(self.selection_population) else ""
            crossover = str(self.crossover_population[i]["ruta"]) if i < len(self.crossover_population) else ""
            mutacion = str(self.mutated_population[i]["ruta"]) if i < len(self.mutated_population) else ""

            # Resaltar los dos cromosomas con el mayor valor de fitness en verde
            if i < 2:
                print(f"\033[92m{cromosomas:<30}{fitness:<20}{seleccion:<30}{crossover:<30}{mutacion:<30}\033[0m")
            else:
                print(f"{cromosomas:<30}{fitness:<20}{seleccion:<30}{crossover:<30}{mutacion:<30}")
