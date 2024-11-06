import random

# Clase Chromosome: genera individuos y población inicial
class Chromosome:
    def __init__(self, n_individuals=2):
        self.n_individuals = n_individuals
        self.population = self.create_population()

    def create_individual(self):
        # Genera un cromosoma con 6 alelos, cada uno con un valor entre 1 y 4
        return [random.randint(1, 4) for _ in range(6)]

    def create_population(self):
        # Crea una población con el número de individuos especificado
        return [self.create_individual() for _ in range(self.n_individuals)]
    
