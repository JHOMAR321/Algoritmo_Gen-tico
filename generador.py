#Generador de cromosomas

# cantidad de cromosoma, cantidad aleatoria acorde a 
# genes que componen son aleatorios 
# maxima cantidad son el maximo de pasos

import random #libreria para generacion aleatoria


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
    
    def construction_poblation (self,max_number_gens):
        for _ in range(self.number_cromosomes):
            cromosome = Cromosome(random.randint(1,max_number_gens))
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


class MultiPoblation:
    def __init__(self, number_poblation):
        self.number_poblation = number_poblation

#generar conjunto de poblaciones
    def generate_poblations (self,max_number_cromosomes,max_number_gens):
        for _ in range(self.number_poblation):
            poblation = Poblation(random.randint(1,max_number_cromosomes))
            poblation.construction_poblation(max_number_gens)
            poblation.draft_poblation()
            print("\n")



#Pruebas de ejecucion
poblaciones = MultiPoblation(5)
poblaciones.generate_poblations(10,6)
#generate_poblations(random.randint(1,5))
#invocacion de la poblacion y su metodo de construccion
#poblacion = Poblation(random.randint(1,10)) # conjunto de cromosomas 
#poblacion.construction_poblation() #construccion de los cromosomas y de sus respectivos genes
#poblacion.draft_poblation() # impresion de los cromosomas y sus genes

