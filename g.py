calls = 0  # Создать переменную вне функций.


def count_calls():  # подсчитывающая вызовы остальных функций. Создать функцию count_calls и
    global calls  # изменять в ней значение переменной calls. Эта функция должна
    calls += 1  # вызываться в остальных двух функциях.


def string_info(string_):
    tuple_ = (len(string_), string_.upper(), string_.lower())
    count_calls()  # Эта функция должна вызываться в остальных двух функциях.
    return tuple_


def is_contains(string_1, list_):  # print(string_1 in list_1 )
    string_1 = str(string_1.upper())
    list_1 = list(map(str.upper, (list_)))  # перевод элементов списка в другой регистр с помощью map
    # print(timeit.timeit(lambda: list(map(str.upper, list_))))
    count_calls()
    return print(string_1 in list_1)

print(string_info('cOpY'))
print(string_info('ArmaDA'))
print(is_contains('мА', ['амам', 'МАма', 'АМАМ']))  # Urban ~ urBAN
print(is_contains('цЦ', ['цыпленок', 'цеце']))  # No matches
print('Вы использовали функции', calls, "раза")

# Вывод на консоль:
# (8, 'CAPYBARA', 'capybara')
# (10, 'ARMAGEDDON', 'armageddon')
# True
# False
# 4
