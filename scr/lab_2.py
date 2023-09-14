import math
from mpmath import csc, sec

# Видаліть усі коментарі, "Unnecessary lines" та підправте код під себе, свій варіант

# Вхідні дані з таблиці, ввести свій варіант
h = 0.2
x_min = 1.5
x_max = 3.5


def calculate_x (min_value: int, max_value: int, step: int):
    x = min_value
    result = 0

    while x <= max_value:

        # з таблиці
        if x < 2:
            # обчислюємо рівняння 1 з таблиці, виводимо результатsc(math.pow(math.e, x))
            print(result)
        # з таблиці
        elif 2 <= x < 3:
            # обчислюємо рівняння 2 з таблиці, виводимо результат
            result = sec(math.log(x))
            print(result)
        # з таблиці
        elif x >= 3:
            # обчислюємо рівняння 3 з таблиці, виводимо результат
            result = math.sin(math.log(x))
            print(result)
        # додаємо до Х - h, крок таблюювання зазначений в таблиці
        x += step


# викликаємо зроблену функцію і передаємо вхідні дані
calculate_x(x_min, x_max, h)
