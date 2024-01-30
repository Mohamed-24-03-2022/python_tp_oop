# -*- coding: utf-8 -*-

import random


def get_grid(lines_count, columns_count, value):
    """ Retourne une grille de 'lines_count' lignes et 'columns_count' colonnes initialisées à 'value'."""
    return [[value]*columns_count for line in range(lines_count)]


def get_random_grid(lines_count, columns_count, values):
    """ Retourne une grille de 'lines_count' lignes et 'columns_count' colonnes initialisés aléatoirement avec des
    valeurs de la liste 'values'."""
    return [[random.choice(values) for _ in range(columns_count)] for _ in range(lines_count)]


def get_lines_count(grid):
    """ Retourne le nombre de lignes de la grille 'grid'."""
    return len(grid)


def get_columns_count(grid):
    """ Retourne le nombre de colonnes de la grille 'grid'."""
    cols = []

    for line in range(len(grid)):
        cols += [len(grid[line])]

    if (not all(i == cols[0] for i in cols)):
        return cols, 'Not a constant columns'

    return cols[0]


def get_line(grid, line_number):
    """ Extrait la ligne numéro 'line_number' de 'grid'."""
    return grid[line_number]


def get_column(grid, column_number):
    """ Extrait la colonne numéro 'column_number' de 'grid'."""
    res = []
    for line in range(len(grid)):
        for col in range(len(grid[line])):
            if (col == column_number):
                res += [grid[line][col]]
    return res


def get_line_str(grid, line_number, separator='\t'):
    """ Retourne la chaine de caractère correspondant à la concaténation des valeurs de la ligne numéro 'line_number' de
    la grille 'grid'. Les caractères sont séparés par le caractère 'separator'."""
    string = ''
    for i, value in enumerate(get_line(grid, line_number)):
        if i+1 == len(grid[line_number]):
            string += f'{value}'
        else:
            string += f'{value}{separator}'
    return string


def get_grid_str(grid, separator='\t'):
    """ Retourne la chaine de caractère représentant la grille 'grid'. Les caractères de chaque ligne de 'grid' sont
    séparés par le caractère 'separator'. Les lignes sont séparées par le caractère de retour à la ligne '\n'."""
    string = ''

    for line in range(len(grid)):
        for value in get_line(grid, line):
            string += f'{value}'

        if line+1 < len(grid):
            string += '\n'
        else:
            string += ''

    return string


def get_diagonal(grid):
    """ Extrait la diagonale de 'grid'."""
    res = []
    for line in range(len(grid)):
        for col in range(len(grid[line])):
            if (line == col):
                res.append(grid[line][col])

    return res


def get_anti_diagonal(grid):
    """ Extrait l'antidiagonale de 'grid'."""

    res = []
    line_init = 0
    grid_init = len(grid[0]) - 1

    for line in range(len(grid)):
        for col in range(len(grid[line])):
            if (line_init > line):
                break
            res.append(grid[line_init][grid_init])
            line_init += 1
            grid_init -= 1

    return res


def has_equal_values(grid, value):
    """ Teste si toutes les valeurs de 'grid' sont égales à 'value'."""

    for line in range(len(grid)):
        for col in range(len(grid[line])):
            if (grid[line][col] != value):
                return False

    return True


def is_square(grid):
    """ Teste si 'grid' a le même nombre de lignes et de colonnes."""
    lines = 0
    cols = 0
    for line in range(len(grid)):
        for col in range(len(grid[line])):
            cols += 1
        lines += 1

    return True if lines == (cols / lines) else False


def get_count(grid, value):
    """ Compte le nombre d'occurrences de 'value' dans 'grid'."""
    count = 0

    for line in range(len(grid)):
        for col in range(len(grid[line])):
            if (grid[line][col] == value):
                count += 1

    return count


def get_sum(grid):
    """ Fait la somme de tous les éléments de 'grid'."""
    sum = 0

    for line in range(len(grid)):
        for col in range(len(grid[line])):
            sum += grid[line][col]

    return sum


def get_coordinates_from_cell_number(grid, cell_number):
    """ Convertit un numéro de case 'cell_number' de 'grid' vers les coordonnées (ligne, colonne) correspondants."""

    line = 0
    i = 0
    for l in range(len(grid)):
        col = 0
        for _ in range(len(grid[l])):
            if i == cell_number:
                break
            col += 1
            i += 1
        if i == cell_number:
            break

        line += 1

    return (line, col)


def get_cell_number_from_coordinates(grid, line_number, column_number):
    """ Converti les coordonnées ('line_number', 'column_number') de 'grid' vers le numéro de case correspondant."""
    line = 0
    cell_number = 0
    for l in range(len(grid)):
        col = 0
        for _ in range(len(grid[l])):
            col += 1
            cell_number += 1
            if (line_number == line and column_number == col):
                return cell_number
        line += 1

    return None


def get_cell(grid, cell_number):
    """ Extrait la valeur de 'grid' en 'cell_number'."""
    line, col = get_coordinates_from_cell_number(grid, cell_number)

    return grid[line][col]


def set_cell(grid, cell_number, value):
    """ Positionne la valeur 'value' dans la case 'cell_number' de 'grid'."""
    line, col = get_coordinates_from_cell_number(grid, cell_number)
    grid[line][col] = value


def get_same_value_cell_numbers(grid, value):
    """ Fourni la liste des numéros des cases à valeur égale à 'value' dans 'grid'."""
    list = []
    i = 0
    for line in range(len(grid)):
        for col in range(len(grid[line])):
            if (grid[line][col] == value):
                list.append(i)

            i += 1

    return list


def get_neighbour(grid, line_number, column_number, delta, is_tore=True):
    """ Retourne le voisin de la cellule 'grid[line_number][column_number]'. La définition de voisin correspond à la
    distance positionnelle indiquée par le 2-uplet 'delta' = (delta_line, delta_column). La case voisine est alors
    grid[line_number + delta_line, column_number + delta_column].
    Si 'is_tore' est à 'True' le voisin existe toujours en considérant 'grid' comme un tore.
    Si 'is_tore' est à 'False' retourne 'None' lorsque le voisin est hors de la grille 'grid'."""

    if (is_tore):
        if (column_number + delta[1] <= get_columns_count(grid) - 1):
            return grid[line_number + delta[0]][column_number + delta[1]]
        elif (column_number + delta[1] > get_columns_count(grid) - 1):
            return grid[line_number + delta[0]][0]

    elif (not is_tore):
        if (column_number + delta[1] <= get_columns_count(grid) - 1):
            return grid[line_number + delta[0]][column_number + delta[1]]
        elif (column_number + delta[1] > get_columns_count(grid) - 1):
            return None


def get_neighborhood(grid, line_number, column_number, deltas, is_tore=True):
    """ Retourne pour la grille 'grid' la liste des N voisins de 'grid[line_number][column_number]' correspondant aux
    N 2-uplet (delta_line, delta_column) fournis par la liste 'deltas'.
    Si 'is_tore' est à 'True' le voisin existe toujours en considérant 'grid' comme un tore.
    Si 'is_tore' est à 'False' un voisin hors de la grille 'grid' n'est pas considéré."""
    neighborhood = []
    for delta in deltas:
        neighborhood.append(get_neighbour(
            grid, line_number, column_number, delta, is_tore))

    return neighborhood


if __name__ == '__main__':
    # Permet de générer toujours le 'même' hasard pour les tests
    random.seed(1000)

    # Constantes de directions
    NORTH, EAST, SOUTH, WEST = (-1, 0), (0, 1), (1, 0), (0, -1)
    NORTH_EAST, SOUTH_EAST, SOUTH_WEST, NORTH_WEST = (
        -1, 1), (1, 1), (1, -1), (-1, -1)
    CARDINAL_POINTS = (NORTH, EAST, SOUTH, WEST)
    WIND_ROSE = (NORTH, NORTH_EAST, EAST, SOUTH_EAST,
                 SOUTH, SOUTH_WEST, WEST, NORTH_WEST)

    # Constantes de test
    LINES_COUNT_TEST, COLUMNS_COUNT_TEST = 5, 7
    LINE_NUMBER_TEST, COLUMN_NUMBER_TEST = 1, 6
    VALUE_TEST = 0
    VALUES_TEST = list(range(2))
    IS_TORE_TEST = True
    DIRECTION_TEST = EAST
    GRID_CONST_TEST = get_grid(
        LINES_COUNT_TEST, COLUMNS_COUNT_TEST, VALUE_TEST)
    GRID_RANDOM_TEST = get_random_grid(
        LINES_COUNT_TEST, COLUMNS_COUNT_TEST, VALUES_TEST)

    # Tests
    assert GRID_CONST_TEST == [[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0]]
    assert GRID_RANDOM_TEST == [[1, 0, 1, 1, 0, 1, 0],
                                [1, 0, 0, 0, 1, 1, 0],
                                [1, 0, 1, 0, 0, 1, 0],
                                [1, 1, 0, 0, 1, 0, 0],
                                [0, 1, 0, 1, 0, 0, 1]]

    assert get_lines_count(GRID_RANDOM_TEST), get_columns_count(GRID_RANDOM_TEST) == (
        LINES_COUNT_TEST, COLUMNS_COUNT_TEST)
    assert get_line_str(GRID_RANDOM_TEST, 2) == "1\t0\t1\t0\t0\t1\t0"
    assert get_grid_str(
        GRID_RANDOM_TEST, '') == "1011010\n1000110\n1010010\n1100100\n0101001"
    assert get_line(GRID_RANDOM_TEST, LINE_NUMBER_TEST) == [
        1, 0, 0, 0, 1, 1, 0]
    assert get_column(GRID_RANDOM_TEST, COLUMN_NUMBER_TEST) == [0, 0, 0, 0, 1]
    assert get_diagonal(GRID_RANDOM_TEST) == [1, 0, 1, 0, 0]
    assert get_anti_diagonal(GRID_RANDOM_TEST) == [0, 1, 0, 0, 0]
    assert has_equal_values(GRID_CONST_TEST, GRID_CONST_TEST[0][0])
    assert not has_equal_values(GRID_RANDOM_TEST, GRID_RANDOM_TEST[0][0])
    assert not is_square(GRID_RANDOM_TEST)
    assert get_count(GRID_RANDOM_TEST, 1) == get_sum(GRID_RANDOM_TEST) == 16
    assert get_coordinates_from_cell_number(GRID_RANDOM_TEST, 13) == (
        LINE_NUMBER_TEST, COLUMN_NUMBER_TEST)
    assert get_cell_number_from_coordinates(
        GRID_RANDOM_TEST, LINE_NUMBER_TEST, COLUMN_NUMBER_TEST) == 13
    assert get_cell(GRID_RANDOM_TEST, 9) == 0
    set_cell(GRID_RANDOM_TEST, 9, 1)
    assert get_cell(GRID_RANDOM_TEST, 9) == 1
    assert get_same_value_cell_numbers(GRID_RANDOM_TEST, 1) == [0, 2, 3, 5, 7, 9, 11, 12, 14, 16, 19, 21, 22, 25, 29,
                                                                31,
                                                                34]
    assert get_neighbour(GRID_RANDOM_TEST, LINE_NUMBER_TEST,
                         COLUMN_NUMBER_TEST, DIRECTION_TEST, IS_TORE_TEST) == 1
    assert not get_neighbour(GRID_RANDOM_TEST, LINE_NUMBER_TEST,
                             COLUMN_NUMBER_TEST, DIRECTION_TEST, not IS_TORE_TEST)
    assert get_neighborhood(GRID_RANDOM_TEST, LINE_NUMBER_TEST, COLUMN_NUMBER_TEST, WIND_ROSE, IS_TORE_TEST) == [0, 1,
                                                                                                                 1,
                                                                                                                 1, 0,
                                                                                                                 1,
                                                                                                                 1, 1]
    assert get_neighborhood(GRID_RANDOM_TEST, LINE_NUMBER_TEST, COLUMN_NUMBER_TEST, WIND_ROSE, not IS_TORE_TEST) == [0,
                                                                                                                     None,
                                                                                                                     None,
                                                                                                                     None,
                                                                                                                     0,
                                                                                                                     1,
                                                                                                                     1,
                                                                                                                     1]
    print("Tests all OK")
