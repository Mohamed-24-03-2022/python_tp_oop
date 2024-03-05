import random
from S06_TP11 import PlanetAlpha
from S07_TP14_01 import Lion, Cow, Water, Herb, Ground


class Main:
    __AUTHORIZED_TYPES = {Lion, Cow, Water, Herb, Ground}

    def __init__(self, planet_name, latitude_cells_count, longitude_cells_count):
        self.__planet_alpha = PlanetAlpha(
            planet_name, latitude_cells_count, longitude_cells_count, Ground())

    def get_planet(self):
        return self.__planet_alpha

    def add_element(self, cell_number, element):
        if (element in self.__AUTHORIZED_TYPES):
            self.__planet_alpha.born(cell_number, element)

    def add_element_random(self, element):
        random_free_place = self.__planet_alpha.get_random_free_place()
        self.__planet_alpha.born(random_free_place, element)

    def populate(self, types_count):
        for element_type, element_count in types_count.items():
            instance = element_type()
            for _ in range(element_count):
                self.add_element_random(instance.__repr__())

    def __repr__(self):
        return self.__planet_alpha.__repr__()


if __name__ == '__main__':
    random.seed(10)
    app = Main("Terre", 5, 10)
    app.populate({Lion: 7, Cow: 3})
    app.populate({Water: 10, Herb: 100})
    print(app)
    nw_neighborhood = app.get_planet().get_cell_neighborhood_numbers(0,
                                                                     PlanetAlpha.WIND_ROSE)
    app.get_planet().die(0)
    for cell in nw_neighborhood:
        app.get_planet().die(cell)
    print(app)
