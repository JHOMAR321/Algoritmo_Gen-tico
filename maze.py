""" File for the maze canvas """
import random
import tkinter as tk
from tkinter import ttk

from robotv2 import Robot


class Maze():
    """ Class to create the maze and the path table
    """

    def __init__(self, length_row, length_column):
        """ Table and maze setup
        """
        self.length_row = length_row
        self.length_column = length_column
        # Initialize the empty array
        self.matrix = [[0 for _ in range(length_column)]
                       for _ in range(length_row)]
        self.root = tk.Tk()
        self.root.title("Maze Generator")
        self.canvas = None
        self.table = None
        self.robot_pos = None
        self.goal_pos = None

    def create_array_object(self, num_objects):
        """ Create array with the objects by placing a 
            given number of obstacles (1s) randomly in the matrix
        """
        objects_added = 0
        while objects_added < num_objects:
            row = random.randint(0, self.length_row - 1)
            col = random.randint(0, self.length_column - 1)

            # Add object only if cell is empty
            if self.matrix[row][col] == 0:
                self.matrix[row][col] = 1
                objects_added += 1

    def generate_matrix(self):
        """ Generates and prints the matrix of 1 and 0
            where 1 means the cell is occupied by an object
            and 0 means it is free
        """
        for row in self.matrix:
            print(row)
        return self.matrix

    def create_canva(self):
        """ Create the canvas where the maze and the table will be housed
        """
        # Delete the existing canvas before creating a new one
        if self.canvas:
            self.canvas.destroy()

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg='white')
        self.canvas.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    def create_maze(self):
        """ Creates the maze where it receives the matrix, 
            reads it and creates the maze according to its 
            dimensions and its objects (1) and free spaces (0)
        """
        # Draw the maze on the canvas
        cell_size = 20  # Size of each cell in pixels
        for row in range(self.length_row):
            for col in range(self.length_column):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                if self.matrix[row][col] == 1:  # If it is an obstacle
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='black')
                else:  # If it is free space
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill='white', outline='gray')

        # Draw the robot (start) and goal (end) positions
        if self.robot_pos:
            x1 = self.robot_pos[1] * cell_size
            y1 = self.robot_pos[0] * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            self.canvas.create_oval(
                x1, y1, x2, y2, fill='green', outline='black')

        if self.goal_pos:
            x1 = self.goal_pos[1] * cell_size
            y1 = self.goal_pos[0] * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            self.canvas.create_oval(
                x1, y1, x2, y2, fill='red', outline='black')

    def create_table(self):
        """ Create the table where the headers are written
        """
        # Drop the existing table before creating a new one
        if self.table:
            self.table.destroy()

        # Create the table below the canvas
        self.table = ttk.Treeview(
            self.root, columns=['#', 'Status'], show="headings")
        self.table.heading('#', text="Cell")
        self.table.heading('Status', text="Status")

        # Add the cells with their values
        for i in range(self.length_row):
            for j in range(self.length_column):
                cell = f"({i},{j})"
                status = "Object" if self.matrix[i][j] == 1 else "Free"
                self.table.insert("", "end", values=(cell, status))

        self.table.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    def update_row_table(self):
        """ Update the table by adding the new rows
        """
        for item in self.table.get_children():
            self.table.delete(item)

        # Reload the table with the current values ​​of the array
        for i in range(self.length_row):
            for j in range(self.length_column):
                cell = f"({i},{j})"
                status = "Object" if self.matrix[i][j] == 1 else "Free"
                self.table.insert("", "end", values=(cell, status))

    def generate_maze_and_update(self):
        """ Generates the maze and updates the canvas and table
        """
        # Getting dimensions from text inputs
        self.length_row = int(self.rows_entry.get())
        self.length_column = int(self.cols_entry.get())

        # Reset the matrix
        self.matrix = [[0 for _ in range(self.length_column)]
                       for _ in range(self.length_row)]

        # Create obstacles
        self.create_array_object(int(self.objects_entry.get()))
        self.generate_matrix()

        # Create or update the canvas and table
        self.create_canva()
        self.create_maze()
        self.create_table()

    def set_robot_and_goal(self):
        """Configurar las posiciones del robot y objetivo y calcular la ruta"""
        robot_row = int(self.robot_row_entry.get())
        robot_col = int(self.robot_col_entry.get())
        goal_row = int(self.goal_row_entry.get())
        goal_col = int(self.goal_col_entry.get())

        # Almacenar las posiciones
        self.robot_pos = (robot_row, robot_col)
        self.goal_pos = (goal_row, goal_col)

        # Instanciar el robot en la posición inicial
        _robot = Robot(self.robot_pos, self.matrix)

        # Definir el conjunto de rutas con sus listas de movimientos
        route_set = {
            'ruta_1': [4, 4, 2, 2],  # Derecha, Derecha, Abajo, Abajo
            'ruta_2': [2, 2, 4, 4],  # Abajo, Abajo, Derecha, Derecha
        }

        # Ejecutar cada ruta en el conjunto de rutas
        for route_name, movements in route_set.items():
            print(f"Ejecutando {route_name}: {movements}")
            # Ejecuta la secuencia de movimientos para la ruta actual
            _robot.get_path(movements)
            # Actualiza el laberinto con la posición del robot
            self.update_robot_position(_robot.path)
            self.create_table()  # Redibuja la tabla para mostrar el laberinto actualizado
            print(f"Ruta {route_name} completada.\n")

            # Restablece la posición del robot para la siguiente ruta
            _robot.reset_position()

    def clear_path(self):
        """ Limpiar la ruta pintada en el canvas """
        # Redibujar el laberinto sin la ruta anterior
        self.create_canva()
        self.create_maze()

    def clear_pathv2(self):
        """Limpiar solo la ruta coloreada en el canvas, dejando los obstáculos, robot y objetivo intactos."""
        cell_size = 20  # Tamaño de cada celda en píxeles

        # Recorre la matriz para encontrar las celdas que forman parte del camino (sin obstáculos, robot o meta)
        for row in range(self.length_row):
            for col in range(self.length_column):
                # Verifica que la celda esté libre (sin obstáculos, robot ni objetivo)
                if self.matrix[row][col] == 0 and (row, col) != self.robot_pos and (row, col) != self.goal_pos:
                    x1 = col * cell_size
                    y1 = row * cell_size
                    x2 = x1 + cell_size
                    y2 = y1 + cell_size
                    # Limpia el rastro (cambiando el color a blanco)
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill='white', outline='gray')

    def update_robot_position(self, robot_path):
        """Actualizar el robot y su ruta en el canvas, dejando un rastro excepto en la celda de inicio."""
        cell_size = 20  # Tamaño de cada celda en píxeles

        # Limpiar la ruta anterior antes de dibujar una nueva
        self.clear_path()

        for idx, step in enumerate(robot_path):
            robot_row, robot_col = step
            x1 = robot_col * cell_size
            y1 = robot_row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            # Pintar la celda solo si no es la celda inicial
            if idx != 0:  # Omitir el primer paso, que es la posición inicial
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill='yellow', outline='gray')  # Color para el rastro

            # Actualizar la tabla si es necesario
            self.update_row_table()

            # Retraso para visualizar el movimiento
            self.root.update()
            self.root.after(500)  # Espera de 500ms entre movimientos

    def mark_cell(self, position, color='lightblue'):
        """Marcar una celda con un color específico para indicar el rastro"""
        cell_size = 20
        row, col = position
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')

    def show_canva(self):
        """ Show the table with the maze """
        # Frame for input fields and buttons to make it cleaner
        input_frame = tk.Frame(self.root)
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        # Row and Column inputs for the maze
        label1 = tk.Label(input_frame, text="Rows:")
        label1.grid(row=0, column=0, padx=5, pady=5)
        self.rows_entry = tk.Entry(input_frame)
        self.rows_entry.grid(row=0, column=1, padx=5, pady=5)
        self.rows_entry.insert(0, str(self.length_row))

        label2 = tk.Label(input_frame, text="Columns:")
        label2.grid(row=0, column=2, padx=5, pady=5)
        self.cols_entry = tk.Entry(input_frame)
        self.cols_entry.grid(row=0, column=3, padx=5, pady=5)
        self.cols_entry.insert(0, str(self.length_column))

        label3 = tk.Label(input_frame, text="Objects:")
        label3.grid(row=1, column=0, padx=5, pady=5)
        self.objects_entry = tk.Entry(input_frame)
        self.objects_entry.grid(row=1, column=1, padx=5, pady=5)
        self.objects_entry.insert(0, "10")

        # Generate Maze button
        generate_button = tk.Button(
            input_frame, text="Generate Maze", command=self.generate_maze_and_update)
        generate_button.grid(row=1, column=2, columnspan=2, pady=5)

        # Robot Start and Goal Position inputs
        label4 = tk.Label(input_frame, text="Robot Start (Row, Column):")
        label4.grid(row=2, column=0, padx=5, pady=5)

        self.robot_row_entry = tk.Entry(input_frame)
        self.robot_row_entry.grid(row=2, column=1, padx=5, pady=5)
        self.robot_row_entry.insert(0, "0")

        self.robot_col_entry = tk.Entry(input_frame)
        self.robot_col_entry.grid(row=2, column=2, padx=5, pady=5)
        self.robot_col_entry.insert(0, "0")

        label5 = tk.Label(input_frame, text="Goal Position (Row, Column):")
        label5.grid(row=3, column=0, padx=5, pady=5)

        self.goal_row_entry = tk.Entry(input_frame)
        self.goal_row_entry.grid(row=3, column=1, padx=5, pady=5)
        self.goal_row_entry.insert(0, "4")

        self.goal_col_entry = tk.Entry(input_frame)
        self.goal_col_entry.grid(row=3, column=2, padx=5, pady=5)
        self.goal_col_entry.insert(0, "4")

        # Set Robot and Goal button
        set_positions_button = tk.Button(
            input_frame, text="Set Robot and Goal", command=self.set_robot_and_goal)
        set_positions_button.grid(row=3, column=3, pady=5)

        # You can add additional sections for the maze visualization
        self.root.mainloop()
