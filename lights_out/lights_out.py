from functools import partial
import tkinter


class Cell(tkinter.Button):

    ON_COLOR = 'yellow'
    OFF_COLOR = 'blue'

    def __init__(self):
        super().__init__()
        self.__state = "on"
        self.turn_on()
        self.configure(command=self.toggle_state)

    def turn_on(self):
        self.__state = "on"
        self.configure(bg=Cell.ON_COLOR)
        self.configure(activebackground=Cell.ON_COLOR)
        self.configure(relief=tkinter.RAISED)

    def turn_off(self):
        self.__state = "off"
        self.configure(bg=Cell.OFF_COLOR)
        self.configure(activebackground=Cell.OFF_COLOR)
        self.configure(relief=tkinter.SUNKEN)

    def toggle_state(self):
        if self.__state == "off":
            self.turn_on()
        else:
            self.turn_off()

    def set_command(self, block):
        def composition():
            self.toggle_state()
            block()
        self.configure(command=composition)


class Game(tkinter.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=None, cnf={}, **kw)
        self.cells = []
        for x in range(self.cells_per_side):
            line = []
            for y in range(self.cells_per_side):
                line.append(self.new_cell_at(x, y))
            self.cells.append(line)

    def new_cell_at(self, x, y):
        c = Cell()
        c.grid(row=x, column=y)
        c.set_command(partial(self.toggle_neighbours_of_cell_at, x, y))
        return c

    def toggle_neighbours_of_cell_at(self, i, j):
        if i >= 1:
            self.cells[i - 1][j].toggle_state()
        if i < self.cells_per_side - 1:
            self.cells[i + 1][j].toggle_state()
        if j >= 1:
            self.cells[i][j - 1].toggle_state()
        if j < self.cells_per_side - 1:
            self.cells[i][j + 1].toggle_state()

    @property
    def cells_per_side(self):
        return 3


if __name__ == "__main__":
    game = Game()
    game.mainloop()
