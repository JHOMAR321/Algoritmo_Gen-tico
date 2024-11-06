""" File for the maze canvas """
import random
import tkinter as tk
from tkinter import ttk


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
        """ Set the robot's starting position and the goal position
        """
        robot_row = int(self.robot_row_entry.get())
        robot_col = int(self.robot_col_entry.get())
        goal_row = int(self.goal_row_entry.get())
        goal_col = int(self.goal_col_entry.get())

        # Store the positions
        self.robot_pos = (robot_row, robot_col)
        self.goal_pos = (goal_row, goal_col)

        # Redraw the maze with the updated positions
        self.create_canva()
        self.create_maze()
        self.create_table()

    def show_canva(self):
        """ Show the table with the maze
        """
        # Add labels and entries for the matrix dimensions and number of objects
        label1 = tk.Label(self.root, text="Rows:")
        label1.grid(row=0, column=0, padx=5, pady=5)

        self.rows_entry = tk.Entry(self.root)
        self.rows_entry.grid(row=0, column=1, padx=5, pady=5)
        self.rows_entry.insert(0, str(self.length_row))

        label2 = tk.Label(self.root, text="Columns:")
        label2.grid(row=0, column=2, padx=5, pady=5)

        self.cols_entry = tk.Entry(self.root)
        self.cols_entry.grid(row=0, column=3, padx=5, pady=5)
        self.cols_entry.insert(0, str(self.length_column))

        label3 = tk.Label(self.root, text="Objects:")
        label3.grid(row=1, column=0, padx=5, pady=5)

        self.objects_entry = tk.Entry(self.root)
        self.objects_entry.grid(row=1, column=1, padx=5, pady=5)
        self.objects_entry.insert(0, "10")

        # Add the "Generate Maze" button
        generate_button = tk.Button(
            self.root, text="Generate Maze", command=self.generate_maze_and_update)
        generate_button.grid(row=1, column=2, columnspan=2, pady=5)

        # Labels and entries for robot and goal positions
        label4 = tk.Label(self.root, text="Robot Start (Row, Column):")
        label4.grid(row=2, column=0, padx=5, pady=5)

        self.robot_row_entry = tk.Entry(self.root)
        self.robot_row_entry.grid(row=2, column=1, padx=5, pady=5)
        self.robot_row_entry.insert(0, "0")

        self.robot_col_entry = tk.Entry(self.root)
        self.robot_col_entry.grid(row=2, column=2, padx=5, pady=5)
        self.robot_col_entry.insert(0, "0")

        label5 = tk.Label(self.root, text="Goal Position (Row, Column):")
        label5.grid(row=3, column=0, padx=5, pady=5)

        self.goal_row_entry = tk.Entry(self.root)
        self.goal_row_entry.grid(row=3, column=1, padx=5, pady=5)
        self.goal_row_entry.insert(0, "4")

        self.goal_col_entry = tk.Entry(self.root)
        self.goal_col_entry.grid(row=3, column=2, padx=5, pady=5)
        self.goal_col_entry.insert(0, "4")

        # Add the "Set Robot and Goal" button
        set_positions_button = tk.Button(
            self.root, text="Set Robot and Goal", command=self.set_robot_and_goal)
        set_positions_button.grid(row=3, column=3, pady=5)

        self.root.mainloop()
        