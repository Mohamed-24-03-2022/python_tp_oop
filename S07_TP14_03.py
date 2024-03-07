import tkinter as tk
from S06_TP11 import PlanetAlpha
from S07_TP14_01 import Lion, Cow, Water, Herb, Ground, Dragon


class Main(tk.Tk):
    __AUTHORIZED_TYPES = {Lion, Cow, Water, Herb, Ground, Dragon}
    __COLORS = {
        'cell_background': 'white',
        'cell_foreground': 'red',
        'grid_lines': 'black',
        'grid_text': 'dark blue',
        'widget_text': 'orange',
    }
    __FONTS = {
        'basic': ('Arial', 16, 'bold'),
    }

    def __init__(self, planet_name, latitude_cell_count, longitude_cell_count, cell_size=50, gutter_size=0, margin_size=10):

        tk.Tk.__init__(self)

        self.__planet_alpha = PlanetAlpha(
            planet_name, latitude_cell_count, longitude_cell_count, Ground())

        self.__cell_size = cell_size
        self.__gutter_size = gutter_size
        self.__margin_size = margin_size

        self.__f_main = tk.Frame(self)
        self.__f_main.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)

        l = self.__planet_alpha.get_lines_count()
        c = self.__planet_alpha.get_columns_count()
        width = c*cell_size + (c-1) * gutter_size + margin_size * 2
        height = l*cell_size + (l-1) * gutter_size + margin_size * 2
        self.__c_draw = tk.Canvas(
            self.__f_main, background=self.__COLORS['cell_background'], width=width, height=height)
        self.__c_draw.pack()

        self.__f_info = tk.Frame(self)
        self.__f_info.pack(side=tk.LEFT, fill=tk.BOTH)

        self.__label_text = tk.StringVar()
        self.__label_text.set('Terre')
        self.__l_element = tk.Label(
            self.__f_info, textvariable=self.__label_text, borderwidth=1, relief="solid", font=self.__FONTS['basic'], fg=self.__COLORS['grid_text'])
        self.__l_element.pack(fill=tk.X)

        self.__lb_elements = tk.Listbox(
            self.__f_info, font=self.__FONTS['basic'])
        self.__lb_elements.pack()

        self.__f_manager = tk.Frame(self.__f_info)
        self.__f_manager.pack()

        self.__b_quit = tk.Button(
            self.__f_manager, text='Close', command=self.quit, fg=self.__COLORS['widget_text'])
        self.__b_quit.pack()

    def get_planet(self):
        return self.__planet_alpha

    def add_element(self, cell_number, element):
        for type in self.__AUTHORIZED_TYPES:
            if (isinstance(element, type)):
                self.__planet_alpha.born(cell_number, element.__repr__())

    def add_element_random(self, element):
        random_free_place = self.__planet_alpha.get_random_free_place()
        self.add_element(random_free_place, element)

    def populate(self, types_count):
        for element_type, element_count in types_count.items():
            instance = element_type()
            for _ in range(element_count):
                self.add_element_random(instance)

    def get_types_count(self):
        res = {}
        for type in self.__AUTHORIZED_TYPES:
            res[type] = self.__planet_alpha.get_count(type().__repr__())
        return res

    def draw_planet(self, grid_lines=True, content=True):
        x0 = self.__margin_size
        y0 = self.__margin_size

        x1 = self.__margin_size + self.__cell_size
        y1 = self.__margin_size + self.__cell_size

        for i in range(self.__planet_alpha.get_lines_count()):
            for j in range(self.__planet_alpha.get_columns_count()):
                x_center = (x0 + x1) / 2
                y_center = (y0 + y1) / 2
                if (grid_lines):
                    self.__c_draw.create_rectangle(
                        x0, y0, x1, y1, fill=self.__COLORS["cell_background"])
                if (content):
                    cell_number = self.__planet_alpha.get_cell_number_from_coordinates(
                        i, j)
                    cell_content = self.__planet_alpha.get_cell(cell_number)

                    self.__c_draw.create_text(
                        x_center, y_center, text=cell_content, fill=self.__COLORS["grid_text"])

                x0 += self.__cell_size + self.__gutter_size
                x1 += self.__cell_size + self.__gutter_size

            x0 = self.__margin_size
            x1 = self.__margin_size + self.__cell_size
            y0 += self.__cell_size + self.__gutter_size
            y1 += self.__cell_size + self.__gutter_size

        if (content):
            cells_number = self.__planet_alpha.get_lines_count(
            ) * self.__planet_alpha.get_columns_count()
            inhabitants_number = 0

            types = self.get_types_count()
            for index, type in enumerate(types):
                if (types[type]):
                    self.__lb_elements.insert(
                        index, f"{types[type]} {type().__class__.__name__}s ({type().__repr__()})")

                inhabitants_number += types[type]

            self.__label_text.set(
                f"Terre\n{inhabitants_number} / {cells_number} inhabitants")

    def __repr__(self):
        return self.__planet_alpha.__repr__()

    def __str__(self):
        return self.__planet_alpha.__str__()


if __name__ == '__main__':
    LINES_COUNT = 20
    COLUMNS_COUNT = 30
    CELL_SIZE = 40
    GUTTER_SIZE = 0
    MARGIN_SIZE = 10

    app = Main("Terre", LINES_COUNT, COLUMNS_COUNT,
               CELL_SIZE, GUTTER_SIZE, MARGIN_SIZE)

    INHABITANTS_TEST = {Lion: 70, Cow: 30}
    RESOURCES_TEST = {Water: 100, Herb: 1000}

    app.populate(INHABITANTS_TEST)
    app.populate(RESOURCES_TEST)

    nw_neighborhood = app.get_planet().get_cell_neighborhood_numbers(0,
                                                                     PlanetAlpha.WIND_ROSE)

    app.get_planet().die(0)

    for cell in nw_neighborhood:
        app.get_planet().die(cell)

    app.draw_planet(False)
    print(app)
    app.mainloop()
