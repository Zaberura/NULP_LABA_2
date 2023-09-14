import math
from mpmath import csc, sec

h = 0.2
x_min = 1.5
x_max = 3.5


def calculate_x (min_value: int, max_value: int, step: int):
    x = min_value

    while x <= max_value:

        if x < 2:
            print(csc(math.pow(math.e, x)))
        elif 2 <= x < 3:
            print(sec(math.log(x)))
        elif x >= 3:
            print(math.sin(math.log(x)))

        x += step


calculate_x(x_min, x_max, h)
