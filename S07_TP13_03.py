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

        self.__c_draw = tk.Canvas(self.__f_main, background='white')
        self.__c_draw.pack()

        self.__b_quit = tk.Button(self, text="Close", command=self.quit)
        self.__b_quit.pack(side=tk.RIGHT)

        # self.draw_grid()

        
        
    
    def draw_grid(self, grid_lines = True, content=True):
        pass


if __name__ == "__main__":
    from S05_TP09_1_template import Grid

    LINES_COUNT = 20
    COLUMNS_COUNT = 30
    GRID_TEST = Grid([[0] * COLUMNS_COUNT for _ in range(LINES_COUNT)])
    GRID_TEST.fill_random(range(10000))

    myApp = MyApp(GRID_TEST)
    myApp.title("Mon application d'affichage d'une grille")
    myApp.mainloop()
