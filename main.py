import tkinter as tk
import math
import random

canvas = None

SQUARE_LENGTH = 100
RADIUS = SQUARE_LENGTH / 2 - 5
POSITION = {"x": 8, "y": 8}
BORDER_WIDTH = 8
NUMBER = 4
LENGTH = SQUARE_LENGTH * NUMBER + BORDER_WIDTH * NUMBER
CELL_COLOR = '#cbbeb5'
BORDER_COLOR = '#b2a698'
tiles = []


class Tile:
    def __init__(self, number, col_number, row_number):
        self.number = number
        self.col_number = col_number
        self.row_number = row_number


def set_field():
    canvas.create_rectangle(POSITION["x"], POSITION["y"], LENGTH + POSITION["x"],
                            LENGTH + POSITION["y"], fill='#cbbeb5', width=BORDER_WIDTH, outline=BORDER_COLOR)

    for i in range(NUMBER - 1):
        x = POSITION["x"] + SQUARE_LENGTH * \
            (i + 1) + BORDER_WIDTH * i + BORDER_WIDTH
        y = POSITION["y"] + SQUARE_LENGTH * \
            (i + 1) + BORDER_WIDTH * i + BORDER_WIDTH
        canvas.create_line(
            x, POSITION["y"], x, LENGTH + POSITION["y"], width=BORDER_WIDTH, fill=BORDER_COLOR)
        canvas.create_line(
            POSITION["x"], y, LENGTH + POSITION["x"], y, width=BORDER_WIDTH, fill=BORDER_COLOR)


def create_canvas():
    root = tk.Tk()
    root.geometry(
        f"""{LENGTH + POSITION["x"] * 2}x{LENGTH + POSITION["y"] * 2}""")
    root.title("2048")
    canvas = tk.Canvas(root, width=(
        LENGTH + POSITION["x"]), height=(LENGTH + POSITION["y"]))
    canvas.place(x=0, y=0)

    return root, canvas


def set_number(num, x, y):
    center_x = POSITION["x"] + BORDER_WIDTH * x + \
        BORDER_WIDTH / 2 + SQUARE_LENGTH * x + SQUARE_LENGTH / 2
    center_y = POSITION["y"] + BORDER_WIDTH * y + \
        BORDER_WIDTH / 2 + SQUARE_LENGTH * y + SQUARE_LENGTH / 2
    canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2,
                            center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill=CELL_COLOR, width=0)
    canvas.create_text(center_x, center_y, text=num,
                       justify="center", font=("", 70), tag="count_text")


def set_tile():
    global tiles
    for i in range(NUMBER):
        for j in range(NUMBER):
            tile = Tile(0, i, j)
            tiles.append(tile)


def show_tile():
    global tiles
    for i in range(NUMBER * NUMBER):
        if tiles[i].number == 0:
            set_number('', tiles[i].col_number, tiles[i].row_number)
        else:
            set_number(tiles[i].number, tiles[i].col_number,
                       tiles[i].row_number)


def add_random_tile():
    global tiles
    random_tile = random.randint(0, NUMBER * NUMBER - 1)
    while tiles[random_tile].number >= 2:
        random_tile = random.randint(0, NUMBER * NUMBER - 1)
    tiles[random_tile].number = 2


def operate(event):
    print(event.keysym)
    add_random_tile()
    show_tile()


def play():
    global canvas
    root, canvas = create_canvas()
    set_field()
    set_tile()
    add_random_tile()
    add_random_tile()
    show_tile()
    root.bind("<Key>", lambda event: operate(event))
    root.mainloop()


play()
