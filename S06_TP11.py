import random
from S05_TP09_1_template import Grid


class PlanetAlpha(Grid):
    NORTH, EAST, SOUTH, WEST = (-1, 0), (0, 1), (1, 0), (0, -1)
    NORTH_EAST, SOUTH_EAST, SOUTH_WEST, NORTH_WEST = (
        -1, 1), (1, 1), (1, -1), (-1, -1)
    CARDINAL_POINTS = (NORTH, EAST, SOUTH, WEST)
    WIND_ROSE = (NORTH, NORTH_EAST, EAST, SOUTH_EAST,
                 SOUTH, SOUTH_WEST, WEST, NORTH_WEST)

    def __init__(self, name, latitude_cells_count, longitude_cells_count, ground):

        GRID_INIT = [[ground for _ in range(longitude_cells_count)]
                     for _ in range(latitude_cells_count)]
        Grid.__init__(self, GRID_INIT)
        self.__name = name
        self.__ground = ground

    def get_name(self):
        return self.__name

    def get_ground(self):
        return self.__ground

    def get_random_free_place(self):
        list = Grid.get_same_value_cell_numbers(self, self.__ground)
        if (len(list) == 0):
            return -1
        return random.choice(list)

    def born(self, cell_number, element):
        line, col = Grid.get_coordinates_from_cell_number(self, cell_number)
        grid = Grid.get_grid(self)
        if (grid[line][col] == self.__ground):
            Grid.set_cell(self, cell_number, element)
            return 1
        return 0

    def die(self, cell_number):
        cell = Grid.get_cell(self, cell_number)
        if (cell != self.__ground):
            Grid.set_cell(self, cell_number, self.__ground)
            return 1
        return 0

    def __repr__(self):
        inhabitants_number = len(Grid.get_same_value_cell_numbers(
            self, self.__ground))
        cells_number = Grid.get_lines_count(
            self) * Grid.get_columns_count(self)

        habitants_list = cells_number - inhabitants_number

        string = f'{self.__name} ({habitants_list} habitants)\n'

        for l in range(Grid.get_lines_count(self)):
            for c in range(Grid.get_columns_count(self)):
                string += Grid.get_grid(self)[l][c]
            string += '\n'

        return string


if __name__ == '__main__':
    random.seed(10)

    PLANET_TEST = PlanetAlpha("Terre", 5, 10, '.')
    INHABITANTS_TEST = {'D': 7, 'C': 3}
    RESOURCES_TEST = {'E': 10, 'H': 20}

    assert PLANET_TEST.get_grid() == [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.',
                                                                                                                                                                                                                                                       '.']]

    print(PLANET_TEST)

    for letter, letter_count in INHABITANTS_TEST.items():
        for _ in range(letter_count):
            free_place = PLANET_TEST.get_random_free_place()
            PLANET_TEST.born(free_place, letter)
    print(PLANET_TEST)

    for letter, letter_count in RESOURCES_TEST.items():
        for _ in range(letter_count):
            free_place = PLANET_TEST.get_random_free_place()
            PLANET_TEST.born(free_place, letter)
    print(PLANET_TEST)

    print(PLANET_TEST.get_neighbour(0, 0, PlanetAlpha.NORTH_WEST))

    print(PLANET_TEST.get_neighborhood(0, 0, PlanetAlpha.CARDINAL_POINTS))

    print(PLANET_TEST.get_neighborhood(0, 0, PlanetAlpha.WIND_ROSE))

    PLANET_TEST.die(0)

    for cell in PLANET_TEST.get_cell_neighborhood_numbers(0, PlanetAlpha.WIND_ROSE):
        PLANET_TEST.die(cell)

    print(PLANET_TEST)

    print(PLANET_TEST. get_neighborhood(0, 0, PlanetAlpha .WIND_ROSE))
