"""
Задача 4. Написать метод, который в консоль выводит таблицу умножения.
На вход метод получает число, до которого выводит таблицу умножения.
В консоли должна появиться таблица.
"""


def multiplication_table(x):
    main_list = []
    first_list = []
    first_list.append('')
    for y in range(1, x+1):
        first_list.append(y)
    main_list.append(first_list)
    for a in range(1, x+1):
        operation_list = []
        for b in range(1, x+1):
            operation_list.append(a*b)
            if b == 1:
                operation_list.append(a * b)
        main_list.append(operation_list)
    test_list = main_list[len(main_list)-1]
    indent_text = len(str(max(test_list)))+2
    for el in main_list:
        text = ''
        for elem in el:
            if type(elem) is int:
                elem = str(elem)
                operation_indent_text = ''
                for num in range(1, indent_text+1):
                    if len(elem) == num:
                        for i in range(0, indent_text-num):
                            operation_indent_text += ' '
                text = text + operation_indent_text + elem
            else:
                operation_indent_text = ''
                for i in range(0, indent_text):
                    operation_indent_text += ' '
                text = text + operation_indent_text + elem
        print(text)


multiplication_table(5)
