# FUNCIONES DE SOPORTE O APOYO EN LA CONFIGURACION DEL LABERINTO Y/O ALGORITMO

# funcion para obtener el valor maximo de genes y cromosomas posibles a generar por la función random
def max_number_gen_cromosome (x_i,y_i,x_u,y_u):
    max_number = abs(x_u-x_i) + abs(y_u-y_i)
    return max_number
