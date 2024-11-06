#Generador de cromosomas

# cantidad de cromosoma, cantidad aleatoria acorde a 
# genes que componen son aleatorios 
# maxima cantidad son el maximo de pasos

import random

def max_number_gen_cromosome (x_i,y_i,x_u,y_u):
    max_number = abs(x_u-x_i) + abs(y_u-y_i)
    return max_number

#number_cromosome = random.randint(1,5) #cambiar el 5 por el valor que devuelva max_number

#cromosomes = []

# llenado de cromosomas 
#def fill_cromosomes():
 #   for _ in range(number_cromosome):
  #      cromosome = []
   #     for _ in range(random.randint(1,10)): #cambiar el 10 por el valor max_number
    #        cromosome.append(random.randint(1,4)) # restringido a la cantidad de pasos
     #   cromosomes.append(cromosome)


#def print_cromosomes():
 #   for i in range(len(cromosomes)):
  #      print(f"Cromosoma {i+1}: {cromosomes[i]}\n")

#-------------------------------------------------------------------------------------------------------------------------------#

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


#fill_cromosomes()
#print_cromosomes()

poblacion = Poblation(random.randint(1,5))
poblacion.construction_poblation()
poblacion.draft_poblation()