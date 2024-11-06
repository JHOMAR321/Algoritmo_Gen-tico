import copy

# Importacion de las clases Chromosome y Algorithm
from chromosome import Chromosome
from algorithm import Algorithm

# Ejecución del algoritmo
if __name__ == "__main__":
    chromosome_instance = Chromosome(n_individuals=4)  # Población inicial de 4 individuos
    algorithm = Algorithm(chromosome_instance.population)

    #Guardamos la población inicial con deepcopy para evitar cambios por referencia
    initial_population = [copy.deepcopy(ind) for ind in algorithm.population]

    # Calculamos fitness de la población inicial
    algorithm.fitness()

    # Selección de los individuos
    selected = algorithm.selection()

    # Cruce (Crossover) para generar nueva población
    crossover_population = algorithm.crossover(selected)

    #Mutación en la nueva población
    mutated_population = algorithm.mutation(crossover_population)

    # Mostrando la tabla de resultados
    algorithm.display_table(initial_population, selected, crossover_population, mutated_population)
