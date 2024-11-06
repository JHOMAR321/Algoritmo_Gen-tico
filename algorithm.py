import random
from chromosome import Chromosome

class GeneticAlgorithm:
    def __init__(self, chromosome_instance, mutation_rate=0.1):
        # Recibe la población generada por una instancia de Chromosome
        self.population = chromosome_instance.population
        self.mutation_rate = mutation_rate  # Tasa de mutación predeterminada del 10%
        self.selection_population = []
        self.crossover_population = []
        self.mutated_population = []

    def mostrar_cromosomas(self):
        # Guardar y mostrar los cromosomas originales
        print("Población original:")
        self.selection_population = self.population.copy()  # Guardar los cromosomas originales
        for individual in self.selection_population:
            print(individual)

    def selection(self):
        # En este ejemplo, la selección no cambia la población, solo la muestra
        print("\nPoblación después de la selección (sin cambios):")
        for individual in self.selection_population:
            print(individual)

    def crossover(self, parent1, parent2):
        # Elegir una posición de cruce aleatoria
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def apply_crossover(self):
        # Generar una nueva población mediante crossover en pares
        new_population = []
        for i in range(0, len(self.selection_population) - 1, 2):
            parent1 = self.selection_population[i]
            parent2 = self.selection_population[i + 1]
            child1, child2 = self.crossover(parent1, parent2)
            new_population.extend([child1, child2])
        if len(self.selection_population) % 2 != 0:
            new_population.append(self.selection_population[-1])
        self.crossover_population = new_population.copy()  # Guardar la población después del crossover
        print("\nPoblación después del crossover:")
        for individual in self.crossover_population:
            print(individual)

    def mutation(self, individual):
        index1 = random.randint(0, len(individual) - 1)
        index2 = random.randint(0, len(individual) - 1)
        individual[index1], individual[index2] = individual[index2], individual[index1]

    def apply_mutation(self):
        # Aplica mutación a cada individuo en la población de crossover
        mutated_population = []
        for individual in self.crossover_population:
            if random.random() < self.mutation_rate:
                self.mutation(individual)
            mutated_population.append(individual)
        self.mutated_population = mutated_population.copy()  # Guardar la población después de la mutación
        print("\nPoblación después de la mutación:")
        for individual in self.mutated_population:
            print(individual)

    def mostrar_tabla(self):
        # Imprimir la tabla en formato manual
        print("\nTabla de Resultados:")
        print(f"{'Cromosomas':<30}{'Selección':<30}{'Crossover':<30}{'Mutación':<30}")
        print("=" * 120)
        for i in range(len(self.selection_population)):
            cromosomas = str(self.selection_population[i])
            seleccion = str(self.selection_population[i]) if i < len(self.selection_population) else ""
            crossover = str(self.crossover_population[i]) if i < len(self.crossover_population) else ""
            mutacion = str(self.mutated_population[i]) if i < len(self.mutated_population) else ""
            print(f"{cromosomas:<30}{seleccion:<30}{crossover:<30}{mutacion:<30}")

# Código principal
if __name__ == "__main__":
    # Crear instancia de Chromosome y generar población
    chromosome_instance = Chromosome()

    # Crear instancia de GeneticAlgorithm pasando la instancia de Chromosome
    genetic_algorithm = GeneticAlgorithm(chromosome_instance, mutation_rate=0.3)

    # Ejecutar las distintas etapas del algoritmo y guardar los resultados en cada etapa
    genetic_algorithm.mostrar_cromosomas()    # Etapa de Cromosomas originales
    genetic_algorithm.selection()             # Etapa de Selección
    genetic_algorithm.apply_crossover()       # Etapa de Crossover
    genetic_algorithm.apply_mutation()        # Etapa de Mutación

    # Mostrar los resultados en una tabla
    genetic_algorithm.mostrar_tabla()
