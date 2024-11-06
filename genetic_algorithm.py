""" Aquí se realiza la lógica para evaluar la mejor ruta en relación al algoritmo genético """
import random
import pandas as pd
from openpyxl.styles import Font, Alignment, PatternFill


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
        self.chromosomes_excel = None

        self.data = []

    def fitness(self, chromosome, min_max_values):
        """
        Calcula el valor de fitness basado en las métricas del cromosoma.

        Args:
            chromosome (dict): Cromosoma con métricas.
            min_max_values (dict): Valores mínimos y máximos de la generación.

        Returns:
            dict: Diccionario con los valores de factibilidad y fitness.
        """
        s_min, s_max = min_max_values["s_min"], min_max_values["s_max"]
        l_min, l_max = min_max_values["l_min"], min_max_values["l_max"]
        t_min, t_max = min_max_values["t_min"], min_max_values["t_max"]

        # Pesos para cada factor
        weight_feasibility = 1.0
        weight_length = 1.0
        weight_turns = 1.0

        # Calcular factores
        feasibility_factor = 1 - \
            ((chromosome["colisiones"] - s_min) / (s_max - s_min + 1))
        length_factor = 1 - \
            ((chromosome["distancia_recorrida"] - l_min) / (l_max - l_min + 1))
        turns_factor = 1 - \
            ((chromosome["giros"] - t_min) / (t_max - t_min + 1))

        # Fitness final
        fitness_value = (
            weight_feasibility * feasibility_factor +
            weight_length * length_factor +
            weight_turns * turns_factor
        )

        # Crear un diccionario con los datos del cromosoma
        chromo_data = {
            "ruta": chromosome["ruta"],
            "distancia_recorrida": chromosome["distancia_recorrida"],
            "cantidad_pasos": chromosome["cantidad_pasos"],
            "colisiones": chromosome["colisiones"],
            "giros": chromosome["giros"],
            "feasibility_factor": feasibility_factor,
            "length_factor": length_factor,
            "turns_factor": turns_factor,
            "fitness": fitness_value
        }

        # Añadir los datos del cromosoma a la lista
        self.data.append(chromo_data)

        # Retornar los factores calculados sin modificar el cromosoma
        return {
            "feasibility_factor": feasibility_factor,
            "length_factor": length_factor,
            "turns_factor": turns_factor,
            "fitness": fitness_value
        }

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
        # Calcular los valores min_max de la generación
        min_max_values = self.calculate_generation_min_max(self.chromosomes)

        # Ordena la población según el valor de fitness, pasando los valores min_max
        best_chromosome = max(self.chromosomes, key=lambda chrom: self.fitness(
            chrom, min_max_values)["fitness"])

        return best_chromosome

    def calculate_generation_min_max(self, chromosomes):
        """
        Calcula los valores mínimos y máximos de distancia, pasos, colisiones y giros en la generación.
        
        Args:
            chromosomes (list of dict): Lista de cromosomas de una generación.
        
        Returns:
            dict: Diccionario con los valores mínimos y máximos.
        """

        print(chromosomes)

        # Comprobar que cada cromosoma es un diccionario y tiene las claves necesarias
        for chrom in chromosomes:
            if not isinstance(chrom, dict):
                print(f"Advertencia: El cromosoma no es un diccionario: {chrom}")
            if "distancia_recorrida" not in chrom or "cantidad_pasos" not in chrom or "colisiones" not in chrom or "giros" not in chrom:
                print(f"Advertencia: Cromosoma incompleto: {chrom}")

        # Ahora procesamos los cromosomas
        distances = [chrom["distancia_recorrida"] for chrom in chromosomes]
        steps = [chrom["cantidad_pasos"] for chrom in chromosomes]
        collisions = [chrom["colisiones"] for chrom in chromosomes]
        turns = [chrom["giros"] for chrom in chromosomes]

        return {
            "s_min": min(collisions), "s_max": max(collisions),
            "l_min": min(distances), "l_max": max(distances),
            "t_min": min(turns), "t_max": max(turns)
        }


    def select_chromosomes(self):
        """
        Selecciona dos cromosomas con el mejor fitness para el crossover.

        Returns:
            tuple: Dos cromosomas seleccionados para la reproducción.
        """
        self.data = []
        # Calcula el fitness para cada cromosoma y agrega esta información
        for chromo in self.chromosomes:
            min_max = self.calculate_generation_min_max(chromo)
            chromo['fitness'] = self.fitness(chromo, min_max)["fitness"]

        # Ordena la población de acuerdo al fitness
        sorted_chromosomes = sorted(
            self.chromosomes, key=lambda chrom: chrom['fitness'], reverse=True)

        # Crear un DataFrame de pandas
        df = pd.DataFrame(self.data)

        # Guardar el DataFrame en un archivo Excel
        df.to_excel("chromosomes_with_fitness.xlsx", index=False)

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
