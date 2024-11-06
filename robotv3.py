""" Lógica del movimiento del robot y actualizar los cromosomas """


class Robot:
    """ Clase del robot que recorre la matriz siguiendo rutas predefinidas en los cromosomas. """

    def __init__(self, matrix, posicion_inicial_robot, posicion_goal_robot):
        """
        Inicializa el robot con la matriz, la posición inicial y el objetivo.

        Args:
            matrix (list): Matriz que representa el entorno del robot.
            posicion_inicial_robot (tuple): Posición inicial del robot (fila, columna).
            posicion_goal_robot (tuple): Posición objetivo del robot (fila, columna).
        """
        self.matrix = matrix
        self.posicion_inicial_robot = posicion_inicial_robot
        self.posicion_goal_robot = posicion_goal_robot
        self.chromosomes = []
        self.path = None

    def mover(self, posicion, movimiento):
        """ Mueve el robot en la matriz según el movimiento especificado.

        Args:
            posicion (tuple): Posición actual del robot (fila, columna).
            movimiento (int): Dirección del movimiento (1 = arriba, 2 = abajo, 3 = izquierda, 4 = derecha).

        Returns:
            tuple: Nueva posición después de realizar el movimiento.
        """
        fila, columna = posicion
        if movimiento == 1:  # Arriba
            fila -= 1
        elif movimiento == 2:  # Abajo
            fila += 1
        elif movimiento == 3:  # Izquierda
            columna -= 1
        elif movimiento == 4:  # Derecha
            columna += 1
        return fila, columna

    def recibir_chromosomas(self, chromosomes):
        """Recibe el diccionario de los cromosomas con sus valores.

        Args:
            chromosomes (list): Lista de cromosomas que contienen rutas y métricas.
        """
        self.chromosomes = chromosomes

    def contar_rutas(self):
        """ Recorre cada ruta en los cromosomas y calcula las métricas de giros, colisiones, distancia y pasos.
        
        Returns:
            list: Lista de cromosomas con métricas actualizadas.
        """
        for chromosome in self.chromosomes:
            posicion_actual = self.posicion_inicial_robot
            distancia_recorrida = 0
            cantidad_pasos = 0
            colisiones = 0
            giros = 0
            direccion_anterior = None

            for movimiento in chromosome["ruta"]:
                # Calcular nueva posición
                nueva_posicion = self.mover(posicion_actual, movimiento)
                fila, columna = nueva_posicion

                # Comprobar si el movimiento es válido dentro de la matriz
                if 0 <= fila < len(self.matrix) and 0 <= columna < len(self.matrix[0]):
                    # Comprobar si hay un obstáculo
                    if self.matrix[fila][columna] == 1:  # Obstáculo
                        colisiones += 1
                    else:
                        # Movimiento válido, incrementar distancia y pasos
                        distancia_recorrida += 1
                        cantidad_pasos += 1
                        posicion_actual = nueva_posicion

                        # Contar giros si cambia la dirección
                        if direccion_anterior is not None and direccion_anterior != movimiento:
                            giros += 1
                        direccion_anterior = movimiento

                        # Verificar si el robot ha alcanzado el objetivo
                        if posicion_actual == self.posicion_goal_robot:
                            print(
                                f"¡Objetivo alcanzado en {cantidad_pasos} pasos!")
                            break  # Terminar el recorrido si llega al objetivo
                else:
                    # Si el movimiento es fuera de los límites, cuenta como colisión
                    colisiones += 1

            # Actualizar métricas en el cromosoma
            chromosome["distancia_recorrida"] = distancia_recorrida
            chromosome["cantidad_pasos"] = cantidad_pasos
            chromosome["colisiones"] = colisiones
            chromosome["giros"] = giros

        return self.chromosomes

    def get_path(self, movements):
        """Recorre la ruta definida por los movimientos y actualiza la posición del robot.

        Args:
            movements (list): Lista de movimientos que indican la ruta a seguir.
        """
        self.path = [self.posicion_inicial_robot]  # Reinicia el camino para cada ruta
        posicion_actual = self.posicion_inicial_robot
        
        for movimiento in movements:
            nueva_posicion = self.mover(posicion_actual, movimiento)
            fila, columna = nueva_posicion

            # Comprueba si la nueva posición está dentro de los límites de la matriz
            if 0 <= fila < len(self.matrix) and 0 <= columna < len(self.matrix[0]):
                if self.matrix[fila][columna] == 0:  # Verifica que no haya un obstáculo
                    posicion_actual = nueva_posicion
                    self.path.append(posicion_actual)  # Agrega la nueva posición a la ruta

            # Detenerse si se alcanza el objetivo
            if posicion_actual == self.posicion_goal_robot:
                break

    def reset_position(self):
        """Reinicia la posición del robot a su posición inicial y limpia la ruta."""
        self.path = [self.posicion_inicial_robot]  # Reinicia la ruta al punto de partida
