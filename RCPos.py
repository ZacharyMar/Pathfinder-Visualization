def get_clicked_pos(pos, rows, width):
    gap = width // rows
    x, y = pos

    row = y // gap
    col = x // gap

    return row, col
