"""
Задача 2. Написать функцию/метод, которая на вход получает массив положительных целых чисел произвольной длины.
Например [42, 12, 18]. На выходе возвращает массив чисел, которые являются общими делителями для всех указанных числе.
В примере это будет [2, 3, 6].
"""


def operation_divisor(operation_list):
    min_number = min(operation_list)
    divisor_list = []
    for el in range(1, min_number + 1):
        count = 0
        for elem in operation_list:
            if elem % el == 0:
                count += 1
        if count == len(operation_list):
            divisor_list.append(el)
    print(divisor_list)


operation_divisor([90, 60, 30])
