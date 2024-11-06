class Robot:
    def __init__(self, start_position, maze):
        self.position = start_position
        self.path = [start_position]
        self.giros = 0
        # 1: arriba, 2: abajo, 3: izquierda, 4: derecha
        self.directions = [1, 2, 3, 4]
        self.total_steps = 0
        self.last_direction = None
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.collisions = 0
        self.turns = 0

        # Copia del laberinto para marcar la ruta del robot
        self.maze_copy = [row[:] for row in maze]

    def move(self, direction):
        x, y = self.position
        prev_position = self.position  # Guardamos la posición anterior en caso de retroceder

        # Mover en cada dirección
        if direction == 1 and x > 0 and self.maze[x - 1][y] != 1:  # Arriba
            self.position = (x - 1, y)
        # Abajo
        elif direction == 2 and x < self.rows - 1 and self.maze[x + 1][y] != 1:
            self.position = (x + 1, y)
        # Izquierda
        elif direction == 3 and y > 0 and self.maze[x][y - 1] != 1:
            self.position = (x, y - 1)
        # Derecha
        elif direction == 4 and y < self.cols - 1 and self.maze[x][y + 1] != 1:
            self.position = (x, y + 1)
        else:
            self.position = prev_position  # Retrocedemos si hay un choque o fuera de límites
            return False  # Indicamos que hubo un choque

        self.path.append(self.position)
        self.total_steps += 1
        return True

    def get_path(self, movements):
        """
        Sigue una secuencia de movimientos, retrocediendo en caso de choques.
        :param movements: Lista de movimientos (1=arriba, 2=abajo, 3=izquierda, 4=derecha).
        """
        for direction in movements:
            # Intentamos mover en la dirección actual
            move_success = self.move(direction)

            # Si el movimiento fue inválido (colisión o fuera de límites), retrocedemos
            if not move_success:
                print(
                    f"Colisión al mover en dirección {direction}, retrocediendo...")
                self.collisions += 1  # Contamos el choque
                # Retrocedemos hacia la dirección opuesta
                if direction == 1:  # Si intentó subir, retrocedemos hacia abajo
                    self.move(2)
                elif direction == 2:  # Si intentó bajar, retrocedemos hacia arriba
                    self.move(1)
                elif direction == 3:  # Si intentó ir a la izquierda, retrocedemos hacia la derecha
                    self.move(4)
                elif direction == 4:  # Si intentó ir a la derecha, retrocedemos hacia la izquierda
                    self.move(3)

            # Después de cada movimiento o retroceso, actualizamos el laberinto
            self.print_maze_with_path()

        print(f"Camino completo: {self.path}")
        print(
            f"Total de pasos: {self.total_steps}, Giros: {self.giros}, Choques: {self.collisions}")

    def print_maze_with_path(self):
        """
        Muestra el laberinto con el camino recorrido.
        """
        maze_copy = [row[:] for row in self.maze]
        for pos in self.path:
            x, y = pos
            maze_copy[x][y] = 2  # Marca el recorrido del robot con el valor 2
        for row in maze_copy:
            print(row)

    def reset_position(self):
        """
        Restablece la posición del robot a la posición inicial y limpia el camino recorrido.
        """
        self.position = self.position  # Restablecemos la posición a la inicial
        self.path = self.path  # Reiniciamos el recorrido
