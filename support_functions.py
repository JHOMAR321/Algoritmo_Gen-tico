# FUNCIONES DE SOPORTE O APOYO EN LA CONFIGURACION DEL LABERINTO Y/O ALGORITMO

# funcion para obtener el valor maximo de genes y cromosomas posibles a generar por la función random
def max_number_gen_cromosome (actual_position,final_position):
    max_number = abs(final_position[0]-actual_position[0]) + abs(final_position[1]-actual_position[1])
    return max_number

def selection_move(option):
    name_move=""
    if(option==1):
        name_move="up"
    elif(option==2):
        name_move="down"
    elif(option==3):
        name_move="left"
    elif(option==4):
        name_move="right"
    return name_move

    