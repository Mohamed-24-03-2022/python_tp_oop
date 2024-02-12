from S02_TP04_template import get_all_letters
import random


class Range:
    def __init__(self, value1, value2):
        self.__lower = min(value1, value2)
        self.__upper = max(value1, value2)

    def get_lower(self):
        return self.__lower

    def get_upper(self):
        return self.__upper

    def to_str(self):
        return f'[{self.__lower},{self.__upper}]'

    def get_size(self):
        return self.__upper - self.__lower

    def get_middle(self):
        return (self.__lower + self.__upper) / 2

    def get_union(self, other):
        new_lower = min(self.__lower, other.get_lower())
        new_upper = max(self.__upper, other.get_upper())
        return Range(new_lower, new_upper)

    def has_intersection(self, other):
        return (other.get_lower() >= self.__lower and other.get_lower() <= self.__upper) or (self.__lower >= other.get_lower() and self.__lower <= other.get_upper())


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def to_str(self):
        return f'({self.__x},{self.__y})'

    def translation(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def get_distance(self, other):
        dx = other.get_x() - self.__x
        dy = other.get_y() - self.__y
        return (dx ** 2 + dy ** 2) ** 0.5


class Segment:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def get_point1(self):
        return self.__point1

    def get_point2(self):
        return self.__point2

    def to_str(self):
        return f'[{self.__point1.to_str()};{self.__point2.to_str()}]'

    def translation(self, dx, dy):
        self.__point1.translation(dx, dy)
        self.__point2.translation(dx, dy)

    def get_length(self):
        return self.__point1.get_distance(self.__point2)

    def get_projection_x(self):
        return Range(self.__point1.get_x(), self.__point2.get_x())

    def get_projection_y(self):
        return Range(self.__point1.get_y(), self.__point2.get_y())

    def get_middle(self):
        mid_x = (self.__point1.get_x() + self.__point2.get_x()) / 2
        mid_y = (self.__point1.get_y() + self.__point2.get_y()) / 2
        return Point(mid_x, mid_y)


class LSystem:
    def __init__(self, axiom, rules):
        self.__axiom = axiom
        self.__rules = rules
        self.__current_steps_count = 0
        self.__current_word = axiom

    def reset(self):
        self.__current_word = self.__axiom
        self.__current_steps_count = 0

    def get_current_word(self):
        return self.__current_word

    def following_state(self):
        print('Current word', self.__current_word)
        print('Current steps count', self.__current_steps_count)

    def generate(self, steps_count):
        for _ in range(steps_count):
            new_word = ''
            for char in self.__current_word:
                if (char in self.__rules):
                    new_word += self.__rules[char]
                else:
                    new_word += char
            self.__current_word = new_word
            self.__current_steps_count += 1
        return self.__current_word


if __name__ == '__main__':
    random.seed(100)

    # Range tests
    range_test1, range_test2 = Range(18.2, 5), Range(10, 20)
    assert range_test1.get_lower() == 5
    assert range_test1.get_upper() == 18.2
    assert range_test2.get_lower() == 10
    assert range_test2.get_upper() == 20

    assert range_test1.to_str() == '[5,18.2]'
    assert range_test2.to_str() == '[10,20]'

    assert range_test1.get_size() == 13.2
    assert range_test2.get_size() == 10

    assert range_test1.get_middle() == 11.6
    assert range_test2.get_middle() == 15

    assert range_test1.get_union(range_test2).to_str() == '[5,20]'
    assert range_test2.get_union(range_test1).to_str() == '[5,20]'

    assert range_test1.has_intersection(range_test2) == True

    # Point tests
    point_test1, point_test2 = Point(1, 1), Point(-1, 1)
    assert point_test1.to_str() == '(1,1)'
    assert point_test2.to_str() == '(-1,1)'
    point_test1.translation(-1, 1)
    assert point_test1.to_str() == '(0,2)'
    assert point_test1.get_distance(point_test2) == 2 ** 0.5

    # Segment tests
    segment_test = Segment(point_test1, point_test2)
    assert segment_test.to_str() == '[(0,2);(-1,1)]'
    segment_test.translation(2, 1)
    assert segment_test.to_str() == '[(2,3);(1,2)]'
    assert segment_test.get_length() == 2 ** 0.5
    assert segment_test.get_projection_x().to_str() == '[1,2]'
    assert segment_test.get_projection_y().to_str() == '[2,3]'
    assert segment_test.get_middle().to_str() == '(1.5,2.5)'

    # LSystem tests
    AXIOM_TEST = 'fx'
    RULES_TEST = {'f': '', 'x': '-fx++fy-', 'y': '+fx--fy+'}

    assert LSystem(AXIOM_TEST, RULES_TEST).generate(
        3) == '---fx++fy-+++fx--fy+-+++-fx++fy---+fx--fy++-'

    print('Tests all OK')
