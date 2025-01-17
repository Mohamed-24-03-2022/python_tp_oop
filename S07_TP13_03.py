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

        l, c = grid.get_lines_count(), grid.get_columns_count()
        width = c*cell_size + (c-1) * gutter_size + margin_size * 2
        height = l*cell_size + (l-1) * gutter_size + margin_size * 2

        self.__c_draw = tk.Canvas(
            self.__f_main,  width=width, height=height, background=self.__COLORS["cell_background"])
        self.__c_draw.pack()

        self.__b_quit = tk.Button(
            self, text="Close", command=self.quit, fg=self.__COLORS["widget_text"], )
        self.__b_quit.pack()

        self.draw_grid()

    def draw_grid(self, grid_lines=True, content=True):
        x0 = self.__margin_size
        y0 = self.__margin_size

        x1 = self.__margin_size + self.__cell_size
        y1 = self.__margin_size + self.__cell_size

        for i in range(self.__grid.get_lines_count()):
            for j in range(self.__grid.get_columns_count()):
                x_center = (x0 + x1) / 2
                y_center = (y0 + y1) / 2
                if (grid_lines):
                    self.__c_draw.create_rectangle(
                        x0, y0, x1, y1, fill=self.__COLORS["cell_background"])
                if (content):
                    cell_number = self.__grid.get_cell_number_from_coordinates(
                        i, j)
                    cell_content = self.__grid.get_cell(cell_number)

                    self.__c_draw.create_text(
                        x_center, y_center, text=cell_content, fill=self.__COLORS["grid_text"])

                x0 += self.__cell_size + self.__gutter_size
                x1 += self.__cell_size + self.__gutter_size

            x0 = self.__margin_size
            x1 = self.__margin_size + self.__cell_size
            y0 += self.__cell_size + self.__gutter_size
            y1 += self.__cell_size + self.__gutter_size


if __name__ == "__main__":
    from S05_TP09_1_template import Grid

    LINES_COUNT = 20
    COLUMNS_COUNT = 30
    GRID_TEST = Grid([[0] * COLUMNS_COUNT for _ in range(LINES_COUNT)])
    GRID_TEST.fill_random(range(10000))
    CELL_SIZE = 30
    GUTTER_SIZE = 5
    MARGIN_SIZE = 10
    myApp = MyApp(GRID_TEST, CELL_SIZE, GUTTER_SIZE, MARGIN_SIZE)
    myApp.title("Mon application d'affichage d'une grille")
    myApp.mainloop()
