import pygame as pg


class Node(object):

    # Colour codes
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PURPLE = (128, 0, 128)
    ORANGE = (255, 165, 0)
    GREY = (128, 128, 128)
    TURQUOISE = (64, 224, 208)

    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = col * width
        self.y = row * width
        self.colour = self.WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):  # Node is used
        return self.colour == self.RED  # Returns bool

    def is_open(self):  # Node is not used
        return self.colour == self.GREEN

    def is_barrier(self):
        return self.colour == self.BLACK

    def is_start(self):
        return self.colour == self.ORANGE

    def is_end(self):
        return self.colour == self.TURQUOISE

    def reset(self):
        self.colour = self.WHITE

    def make_closed(self):
        self.colour = self.RED

    def make_open(self):
        self.colour = self.GREEN

    def make_barrier(self):
        self.colour = self.BLACK

    def make_start(self):
        self.colour = self.ORANGE

    def make_end(self):
        self.colour = self.TURQUOISE

    def make_path(self):
        self.colour = self.PURPLE

    def draw(self, win):
        pg.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

    # Creates list of open neighbouring nodes
    def update_neighbours(self, grid):
        self.neighbours = []
        # Check node above
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbours.append(grid[self.row - 1][self.col])
        # Check node below
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbours.append(grid[self.row + 1][self.col])
        # Check node left
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbours.append(grid[self.row][self.col - 1])
        # Check node right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbours.append(grid[self.row][self.col + 1])
