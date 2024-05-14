"""
Задача 3. Написать функцию/метод, которая возвращает массив простых чисел
в диапазоне (2 числа - минимальное и максимальное) заданных чисел.
Например, на вход переданы 2 числа: от 11 до 20  (диапазон считается включая граничные значения).
На выходе программа должна выдать [11, 13 , 17, 19]
"""


def prime_number(num_1, num_2):
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    operation_list = []
    for el in range(num_1, num_2+1):
        count = 0
        for elem in range(1, el+1):
            if el % elem == 0:
                count += 1
        if count == 2:
            operation_list.append(el)
    print(operation_list)


prime_number(11, 20)
