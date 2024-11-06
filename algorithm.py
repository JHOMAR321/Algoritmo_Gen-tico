import random
from chromosome import Chromosome

class GeneticAlgorithm:
    """
    Implementa un Algoritmo Genético con funciones de selección, crossover y mutación.
    """
    def __init__(self, chromosome_instance, mutation_rate=0.1):
        # Recibe la población generada por una instancia de Chromosome
        self.population = chromosome_instance.population
        self.mutation_rate = mutation_rate
        self.selection_population = []
        self.crossover_population = []
        self.mutated_population = []
        self.fitness_scores = []

    def fitness(self, wf=3, wl=2, wd=1):
        """
        Calcula el fitness para cada individuo de la población usando factores ponderados
        de colisiones, pasos y distancia.
        
        wf : factor de factibilidad
        wl : factor de longitud
        wd : factor de distancia al destino
        """
        # Calcula el fitness para cada individuo
        self.fitness_scores = []
        for individual in self.population:
            # Simulación de cálculo de 'colisiones', 'pasos' y 'distancia_a_Y'
            colisiones = random.randint(0, 3)
            pasos = random.randint(6, 12)
            distancia_a_Y = random.randint(0, 6)

            # Cálculo de factores de fitness
            factibilidad = 1 - (colisiones - 0) / (3 - 0)
            longitud = 1 - (pasos - 6) / (12 - 6)
            destino = 1 - (distancia_a_Y - 0) / (6 - 0)

            # Fitness total ponderado
            fitness_total = (wf * factibilidad + wl * longitud + wd * destino) / (wf + wl + wd)
            self.fitness_scores.append(fitness_total)

        print("\nFitness de cada cromosoma:")
        for i, score in enumerate(self.fitness_scores):
            print(f"Cromosoma {i + 1}: {self.population[i]}, Fitness Total: {score}")

    def mostrar_cromosomas(self):
        """Muestra la población original."""
        print("Población original:")
        self.selection_population = self.population.copy()
        for individual in self.selection_population:
            print(individual)

    def selection(self):
        """Realiza el proceso de selección (en este caso, selecciona sin cambios)."""
        print("\nPoblación después de la selección (sin cambios):")
        for individual in self.selection_population:
            print(individual)

    def crossover(self, parent1, parent2):
        """
        Realiza el crossover entre dos padres en un punto aleatorio.

        Args:
            parent1 (list): Primer cromosoma.
            parent2 (list): Segundo cromosoma.
        """    
        crossover_point = random.randint(1, len(parent1) - 1)
        print("Antes del crossover:")
        print("Padre 1:", parent1)
        print("Padre 2:", parent2)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point:] + parent1[crossover_point:]
        print("\nDespués del crossover:")
        print("Hijo 1:", child1)
        print("Hijo 2:", child2)
        return child1, child2

    def apply_crossover(self):
        """
         Aplica el crossover a la población seleccionada y genera una nueva población.
        """
        new_population = []
        for i in range(0, len(self.selection_population) - 1, 2):
            parent1 = self.selection_population[i]
            parent2 = self.selection_population[i + 1]
            child1, child2 = self.crossover(parent1, parent2)
            new_population.extend([child1, child2])
        if len(self.selection_population) % 2 != 0:
            new_population.append(self.selection_population[-1])
        self.crossover_population = new_population.copy()
        print("\nPoblación después del crossover:")
        for individual in self.crossover_population:
            print(individual)

    def mutation(self, individual):
        """
        Realiza una mutación en los genes de un cromosoma con base en la tasa de mutación.

        Args:
            individual (list): Cromosoma que será mutado.
        """
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                # Cambiar el valor del gen actual de forma aleatoria
                original_gene = individual[i]
                individual[i] = random.randint(1, 4)  # Asumiendo valores entre 1 y 4 para cada gen
                print(f"Mutación: Cambió el gen en la posición {i} de {original_gene} a {individual[i]}")

    def apply_mutation(self):
        """Aplica mutaciones a la población después del crossover."""
        mutated_population = []
        for individual in self.crossover_population:
            mutated_individual = individual[:]
            self.mutation(mutated_individual)
            mutated_population.append(mutated_individual)
        self.mutated_population = mutated_population.copy()
        print("\nPoblación después de la mutación:")
        for individual in self.mutated_population:
            print(individual)

    def mostrar_tabla(self):
        """Muestra una tabla de resultados con los cromosomas, selección, crossover, mutación y fitness."""
        print("\nTabla de Resultados:")
        print(f"{'Cromosomas':<30}{'Fitness':<20}{'Selección':<30}{'Crossover':<30}{'Mutación':<30}")
        print("=" * 135)
        for i in range(len(self.selection_population)):
            cromosomas = str(self.selection_population[i])
            seleccion = str(self.selection_population[i]) if i < len(self.selection_population) else ""
            fitness = f"{self.fitness_scores[i]:.2f}" if i < len(self.fitness_scores) else ""
            crossover = str(self.crossover_population[i]) if i < len(self.crossover_population) else ""
            mutacion = str(self.mutated_population[i]) if i < len(self.mutated_population) else ""
            print(f"{cromosomas:<30}{fitness:<20}{seleccion:<30}{crossover:<30}{mutacion:<30}")