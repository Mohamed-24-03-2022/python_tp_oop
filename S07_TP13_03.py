import tkinter as tk


class MyApp(tk.Tk):
    __COLORS = {
        "cell_background": "white",
        "cell_foreground": "red",
        "grid_lines": "black",
        "grid_text": "dark blue",
        "widget_text": "orange",
    }

    def __init__(self, grid, cell_size=50, gutter_size=0, margin_size=10):
        tk.Tk.__init__(self)

        self.__grid = grid
        self.__cell_size = cell_size
        self.__gutter_size = gutter_size
        self.__margin_size = margin_size

        self.__f_main = tk.Frame(self)
        self.__f_main.pack()

        width = grid.get_columns_count()*(cell_size+gutter_size) + margin_size * 2
        # height = grid.get_lines_count()*(cell_size+gutter_size) + margin_size * 2
        self.__c_draw = tk.Canvas(
            self.__f_main, background='white', width=width, height=600)
        self.__c_draw.pack()

        self.__b_quit = tk.Button(
            self, text="Close", command=self.quit, fg=self.__COLORS["widget_text"], )
        self.__b_quit.pack(side=tk.BOTTOM)

        self.draw_grid()

    def draw_grid(self, grid_lines=True, content=True):
        x0 = self.__margin_size
        y0 = self.__margin_size

        x1 = self.__margin_size + self.__cell_size
        y1 = self.__margin_size + self.__cell_size

        x_center = (x0 + x1) / 2
        y_center = (y0 + y1) / 2

        if (grid_lines):
            for i in range(self.__grid.get_lines_count()):
                for j in range(self.__grid.get_columns_count()):
                    self.__c_draw.create_rectangle(
                        x0, y0, x1, y1, fill=self.__COLORS["cell_background"])

                    if (content):
                        self.__c_draw.create_text(
                            x_center, y_center, text=self.__grid.get_cell(i+j), fill=self.__COLORS["grid_text"])

                    x0 += self.__cell_size + self.__gutter_size
                    x1 += self.__cell_size + self.__gutter_size
                    x_center = (x0 + x1) / 2

                x0 = self.__margin_size
                x1 = self.__margin_size + self.__cell_size
                y0 += self.__cell_size + self.__gutter_size
                y1 += self.__cell_size + self.__gutter_size
                x_center = (x0 + x1) / 2
                y_center = (y0 + y1) / 2


if __name__ == "__main__":
    from S05_TP09_1_template import Grid

    LINES_COUNT = 20
    COLUMNS_COUNT = 30
    GRID_TEST = Grid([[0] * COLUMNS_COUNT for _ in range(LINES_COUNT)])
    GRID_TEST.fill_random(range(10000))
    CELL_SIZE = 50
    GUTTER_SIZE = 5
    MARGIN_SIZE = 10
    myApp = MyApp(GRID_TEST, CELL_SIZE, GUTTER_SIZE, MARGIN_SIZE)
    myApp.title("Mon application d'affichage d'une grille")
    myApp.mainloop()
