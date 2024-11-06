from chromosome_v3 import Chromosome
from genetic_algorithm_v2 import GeneticAlgorithm

if __name__ == "__main__":
    # Instancia de Chromosome para generar la población inicial
    chromosome_instance = Chromosome(n_individuals=4) # individuos utilizados: 4

    # Crear una instancia de GeneticAlgorithm pasando la instancia de Chromosome
    genetic_algorithm = GeneticAlgorithm(chromosome_instance, mutation_rate=0.3)

    # Ejecutar las distintas etapas del algoritmo genético
    genetic_algorithm.mostrar_cromosomas()    # Mostrar cromosomas originales
    genetic_algorithm.fitness()               # Calcular el fitness de cada cromosoma
    genetic_algorithm.selection()             # Realizar selección
    genetic_algorithm.apply_crossover()       # Realizar crossover
    genetic_algorithm.apply_mutation()        # Aplicar mutación

    # Mostrar los resultados en formato de tabla
    genetic_algorithm.mostrar_tabla()
