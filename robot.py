class Robot:
    def __init__(self, start_position, maze):
        """
        Se inicialia el robot en la posición de inicio y el laberinto.
        El robot comenzará en la posición especificada y tendrá acceso al laberinto.
        
        :param start_position: Tupla (x, y) con la posición inicial del robot.
        :param maze: Lista bidimensional que representa el laberinto, donde 0 es un espacio libre y 1 es un obstáculo.
        """
        self.position = start_position  # La posición actual del robot en el laberinto.
        self.path = [start_position]  # Lista que contiene el recorrido del robot hasta el momento.
        self.giros = 0  # Contador de giros realizados por el robot.
        self.directions = ['up', 'down', 'left', 'right']  # Lista de las direcciones posibles de movimiento.
        self.total_steps = 0  # Contador de pasos totales dados por el robot.
        self.last_direction = None  # Dirección del último movimiento realizado.
        self.maze = maze  # Laberinto representado como una matriz (0 = espacio libre, 1 = obstáculo).
        self.rows = len(maze)  # Número de filas en el laberinto.
        self.cols = len(maze[0])  # Número de columnas en el laberinto.
        self.path_length = 0  # Longitud total del camino recorrido por el robot.

    def move(self, direction):
        """
        Mueve el robot en la dirección especificada, si es posible.
        Verifica si el movimiento es válido (dentro de los límites y sin obstáculos).
        
        :param direction: La dirección a la que se quiere mover el robot. Puede ser 'up', 'down', 'left', 'right'.
        """
        x, y = self.position  # Extraemos la posición actual del robot.
        
        # Condiciones para moverse hacia arriba, abajo, izquierda o derecha, según la dirección solicitada.
        if direction == 'up' and x > 0 and self.maze[x - 1][y] != 1:
            self.position = (x - 1, y)  # Mover hacia arriba.
        elif direction == 'down' and x < self.rows - 1 and self.maze[x + 1][y] != 1:
            self.position = (x + 1, y)  # Mover hacia abajo.
        elif direction == 'left' and y > 0 and self.maze[x][y - 1] != 1:
            self.position = (x, y - 1)  # Mover hacia la izquierda.
        elif direction == 'right' and y < self.cols - 1 and self.maze[x][y + 1] != 1:
            self.position = (x, y + 1)  # Mover hacia la derecha.
        else:
            # Si el movimiento es inválido (fuera de límites o con un obstáculo en esa dirección).
            if direction == 'right' and y < self.cols - 1:
                print(f"Movimiento '{direction}' inválido: Obstáculo en {self.position[0], y + 1}.")
            elif direction == 'right':
                print(f"Movimiento '{direction}' inválido: Fuera de límites en {self.position[0], y + 1}.")
            return  # El movimiento no se realiza si es inválido.
        
        # Si el movimiento es válido, actualizamos el recorrido y contadores.
        self.path.append(self.position)  # Añadimos la nueva posición al recorrido.
        self.total_steps += 1  # Incrementamos el contador de pasos.
        self.path_length += 1  # Incrementamos la longitud del camino.
        
        # Detectamos un giro si la dirección ha cambiado con respecto al último movimiento.
        if self.last_direction and self.last_direction != direction:
            self.giros += 1  # Incrementamos el contador de giros.
        self.last_direction = direction  # Actualizamos la última dirección.

    def is_feasible(self):
        """
        Comprueba si el camino del robot es viable (sin obstáculos).
        Recorre el camino del robot y verifica si hay obstáculos en las posiciones visitadas.
        
        :return: True si el camino es viable, False si hay algún obstáculo en el camino.
        """
        for position in self.path:
            x, y = position
            if self.maze[x][y] == 1:  # Verifica si el robot ha tocado un obstáculo.
                return False  # Si hay un obstáculo, el camino no es viable.
        return True  # Si no hay obstáculos, el camino es viable.

    def evaluate_object(self, population_metrics):
        """
        Evalúa los factores de aptitud del robot según su desempeño.
        Calcula tres factores: viabilidad (Ff), longitud (Fl) y número de giros (Ft).
        
        :param population_metrics: Diccionario con las métricas de la población (mínimos y máximos de pasos, longitud y giros).
        :return: Los tres factores de aptitud (Ff, Fl, Ft).
        """
        Smin, Smax = population_metrics['Smin'], population_metrics['Smax']
        Lmin, Lmax = population_metrics['Lmin'], population_metrics['Lmax']
        Tmin, Tmax = population_metrics['Tmin'], population_metrics['Tmax']
        
        # Factor de viabilidad Ff: Mide si el robot ha recorrido un camino sin obstáculos.
        S = self.total_steps if self.is_feasible() else float('inf')  # Si el camino es viable, usamos los pasos, de lo contrario, usamos infinito.
        Ff = 1 - (S - Smin) / (Smax - Smin) if S != float('inf') else 0  # Calcula el factor de viabilidad.

        # Factor de longitud Fl: Mide la longitud del camino recorrido, se quiere que sea lo más corto posible.
        L = self.path_length
        Fl = 1 - (L - Lmin) / (Lmax - Lmin)  # Calcula el factor de longitud.

        # Factor de giros Ft: Mide cuántos giros ha hecho el robot, se quiere minimizar el número de giros.
        T = self.giros
        Ft = 1 - (T - Tmin) / (Tmax - Tmin)  # Calcula el factor de giros.

        return Ff, Fl, Ft  # Devuelve los tres factores de aptitud.
