import math

# Видаліть усі коментарі, "Unnecessary lines" та підправте код під себе


# вхідні дані з табдиці
a = -1
b = -0.9
h = 0.01
d = 0.001

# список для збереження результатів
results_table = []


# функція всередині сігми, ВСТАВИТИ СВОЄ РІВНЯННЯ
def func_for_k(par1, par2):
    return (math.pow(-1, par1) * par2)/(par1 * (par1 + 1)) * math.sin(par1 * par2)


# функція для обробки рівняння
def calculate_equation(x_min, x_max, step, ms):

    # задаємо початковий Х
    x = x_min

    # перевірка на те, аби Х не виходив за заданий в таблиці діапазон
    while x <= x_max:

        # задаємо початковий К, те що під знаком Сігми
        k = 2
        # змінна в якій зберігатиметься сума розрахунків
        total = 0

        # рахуємо і додаємо відповіді до загальної суми (total) допоки
        # відповіді не стануть меншими за похибку (з табл.) (за модулем).

        # while - перевіряє чи не менший результат за модулем за похибку (у мене 0.001)
        while abs(func_for_k(k, x)) >= ms:

            # Unnecessary line
            print('K is ' + str(k) + '+ and X is ' + str(x) + ' f(k) = ' + str(func_for_k(k, x)))

            # додаємо крок табуляції до загальної суми
            total += func_for_k(k, x)
            # збільшуємо К на 1, переходимо на наст. коло обчислень
            k += 1

        # виводимо результат обчислень Сігми
        print('Результат: ' + str(total))

        # Unnecessary line
        results_table.append(total)

        # Робимо крок по Х на значення яке зазначене в таблиці
        x += step


# запускаємо написану вище функцію і передаємо у неї значення з таблиці: a, b, h, d
calculate_equation(a, b, h, d)

# Unnecessary line
for items in results_table:
    print(items)
