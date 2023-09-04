import Node
import pygame as pg


def make_grid(rows, width):
    grid = []
    gap = width // rows

    # Create rows
    for i in range(rows):
        grid.append([])

        # Create Columns - each coloumn of row i will have a node
        for j in range(rows):
            node = Node.Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


def draw_grid(win, rows, width):
    gap = width // rows

    for i in range(rows):
        pg.draw.line(win, (128, 128, 128), (0, i * gap), (width, i * gap))

    for j in range(rows):
        pg.draw.line(win, (128, 128, 128), (j * gap, 0), (j * gap, width))
