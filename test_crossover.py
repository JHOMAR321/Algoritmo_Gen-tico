import random


def crossover(arr1, arr2):
    # Elegir una posición aleatoria
    crossover_point = random.randint(1, len(arr1) - 1)

    # Mostrar los arreglos antes del crossover
    print("Antes del crossover:")
    print("Arreglo 1:", arr1)
    print("Arreglo 2:", arr2)

    # Realizar el crossover
    new_arr1 = arr1[:crossover_point] + arr2[crossover_point:]
    new_arr2 = arr2[:crossover_point] + arr1[crossover_point:]

    # Mostrar los arreglos después del crossover
    print("\nDespués del crossover:")
    print("Nuevo arreglo 1:", new_arr1)
    print("Nuevo arreglo 2:", new_arr2)

    return new_arr1, new_arr2


def mutation(arr):
    # Seleccionar dos posiciones aleatorias en el arreglo
    index1 = random.randint(0, len(arr) - 1)
    index2 = random.randint(0, len(arr) - 1)

    # Mostrar el arreglo antes de la mutación
    print("\nAntes de la mutación:")
    print("Arreglo:", arr)

    # Realizar la mutación intercambiando los valores de las dos posiciones
    arr[index1], arr[index2] = arr[index2], arr[index1]

    # Mostrar el arreglo después de la mutación
    print("Después de la mutación:")
    print("Arreglo:", arr)


# Ejemplo de uso
arr1 = [1, 2, 3, 4]
arr2 = [4, 3, 2, 1]

# Realizar el crossover
new_arr1, new_arr2 = crossover(arr1, arr2)

# Realizar la mutación en ambos arreglos resultantes
mutation(new_arr1)
mutation(new_arr2)
