#Generador de cromosomas

# cantidad de cromosoma, cantidad aleatoria acorde a 
# genes que componen son aleatorios 
# maxima cantidad son el maximo de pasos

import random 

def max_number_gen_cromosome (x_i,y_i,x_u,y_u):
    max_number = abs(x_u-x_i) + abs(y_u-y_i)
    return max_number

class Cromosome:
    # Constructor
    def __init__(self, number_gens):
        self.number_gens = number_gens  # Atributo de instancia
        self.total_gens = [] 
    
    def construction_cromosome(self):
        for _ in range(self.number_gens): 
            gen = random.randint(1,4)
            self.total_gens.append(gen) 
        

    def draft_cromosome (self):
        print("[", end=" ")
        for gen in self.total_gens:
            print(gen, end=" ")
        print("]")



class Poblation:
    def __init__(self, number_cromosomes):
        self.number_cromosomes = number_cromosomes
        self.total_cromosomes = []
    
    def construction_poblation (self):
        for _ in range(self.number_cromosomes):
            cromosome = Cromosome(random.randint(1,10))
            cromosome.construction_cromosome()
            self.total_cromosomes.append(cromosome)

    def draft_poblation (self):
        for cromosome in self.total_cromosomes:
            print("Cromosoma: ")
            cromosome.draft_cromosome()



poblacion = Poblation(random.randint(1,5))
poblacion.construction_poblation()
poblacion.draft_poblation()