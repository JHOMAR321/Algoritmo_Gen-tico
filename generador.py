#Generador de cromosomas

# cantidad de cromosoma, cantidad aleatoria acorde a 
# genes que componen son aleatorios 
# maxima cantidad son el maximo de pasos

import random #libreria para generacion aleatoria

# funcion para obtener el valor maximo de genes y cromosomas posibles a generar por la función random
def max_number_gen_cromosome (x_i,y_i,x_u,y_u):
    max_number = abs(x_u-x_i) + abs(y_u-y_i)
    return max_number

# funcion para generar cromosomas aleatorios
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
        print("[", end="")
        i=0
        for gen in self.total_gens:
            if(i<(len(self.total_gens)-1)):
                print(gen,end=",")
            else:
                print(gen, end="")
            i=i+1
        print("]",end="")


# funcion para generar el conjunto aleatorio de cromosomas
class Poblation:
    def __init__(self, number_cromosomes):
        self.number_cromosomes = number_cromosomes
        self.total_cromosomes = []
    
    def construction_poblation (self):
        for _ in range(self.number_cromosomes):
            cromosome = Cromosome(random.randint(1,6))
            cromosome.construction_cromosome()
            self.total_cromosomes.append(cromosome)

    def draft_poblation (self):
        i=0
        print("[")
        for cromosome in self.total_cromosomes:
            if(i<(len(self.total_cromosomes)-1)):
                cromosome.draft_cromosome()
                print(",",end="\n")
            else:
                cromosome.draft_cromosome()
            i=i+1
        print("\n]")    



#generar conjunto de poblaciones
def generate_poblations (number_poblation):
   for _ in range(number_poblation):
       #print(f"Poblacion {i+1}:\n")
       poblation = Poblation(random.randint(1,10))
       poblation.construction_poblation()
       poblation.draft_poblation()
       print("\n")
generate_poblations(random.randint(1,5))


#invocacion de la poblacion y su metodo de construccion
#poblacion = Poblation(random.randint(1,10)) # conjunto de cromosomas 
#poblacion.construction_poblation() #construccion de los cromosomas y de sus respectivos genes
#poblacion.draft_poblation() # impresion de los cromosomas y sus genes

