import Grid
import pygame as pg


def draw(win, grid, rows, width):
    win.fill((255, 255, 255))

    Grid.draw_grid(win, rows, width)

    for row in grid:
        for node in row:
            node.draw(win)

    Grid.draw_grid(win, rows, width)
    pg.display.update()
