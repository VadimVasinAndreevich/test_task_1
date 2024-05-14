"""
Задача 1. Разработайте функцию, которая принимает целое число в качестве аргумента и возвращает строку, содержащую
это число и слово "компьютер" в нужном склонении по падежам в зависимости от числа.
Например, при вводе числа 25 функция должна возвращать "25 компьютеров", для числа 41 — "41 компьютер",
а для числа 1048 — "1048 компьютеров".
"""


def computer_operation(number):
    number_str = str(number)
    text = ''
    if number == 0 or 5 <= number <= 20:
        text = number_str + ' компьютеров'
    elif number == 1:
        text = number_str + ' компьютер'
    elif 2 <= number <= 4:
        text = number_str + ' компьютера'
    elif len(number_str) == 2:
        if int(number_str[-1]) == 0 or 5 <= int(number_str[-1]) <= 9:
            text = number_str + ' компьютеров'
        elif int(number_str[-1]) == 1:
            text = number_str + ' компьютер'
        elif 2 <= int(number_str[-1]) <= 4:
            text = number_str + ' компьютера'
    elif len(number_str) >= 3:
        if int(number_str[-2]) == 0 and int(number_str[-1]) == 0 or 5 <= int(number_str[-1]) <= 9:
            text = number_str + ' компьютеров'
        elif int(number_str[-2]) == 0 and int(number_str[-1]) == 1:
            text = number_str + ' компьютер'
        elif int(number_str[-2]) == 0 and 2 <= int(number_str[-1]) <= 4:
            text = number_str + ' компьютера'
        elif int(number_str[-2]) == 1:
            text = number_str + ' компьютеров'
        elif int(number_str[-2]) >= 2 and int(number_str[-1]) == 0 or 5 <= int(number_str[-1]) <= 9:
            text = number_str + ' компьютеров'
        elif int(number_str[-2]) >= 2 and int(number_str[-1]) == 1:
            text = number_str + ' компьютер'
        elif int(number_str[-2]) >= 2 and 2 <= int(number_str[-1]) <= 4:
            text = number_str + ' компьютера'
    print(text)


computer_operation(0)
computer_operation(1)
computer_operation(2)
computer_operation(6)
computer_operation(12)
computer_operation(21)
computer_operation(22)
computer_operation(27)
computer_operation(100)
computer_operation(101)
computer_operation(102)
computer_operation(107)
computer_operation(113)
computer_operation(121)
computer_operation(122)
computer_operation(134)
computer_operation(130)
computer_operation(131)
computer_operation(138)
