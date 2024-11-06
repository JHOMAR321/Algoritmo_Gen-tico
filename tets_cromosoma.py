from chromosomev2 import Chromosome

# Definimos una matriz de 5x5 y posiciones de inicio y fin
length_row, length_column = 8, 9
posicion_robot = (0, 0)  # Posición inicial
posicion_goal = (7, 8)   # Posición objetivo
num_chromosomes = 5      # Número de cromosomas a generar

# Crear instancia de Chromosome
chromosome_creator = Chromosome(
    length_row, length_column, posicion_robot, posicion_goal, num_chromosomes)

# Generar y mostrar los cromosomas
chromosomes = chromosome_creator.generate_chromosomes()

print("Cromosomas : ", chromosomes)

for i, chromo in enumerate(chromosomes, start=1):
    print(f"Cromosoma {i}: {chromo}")
