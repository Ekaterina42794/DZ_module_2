import random  # для подсчета скорости выполнения#
from string import ascii_lowercase  # для подсчета скорости выполнения#
import timeit  # для подсчета скорости выполнения#

from module_2_hard import result

calls = 0  # Создать переменную вне функций.


def count_calls():  # подсчитывающая вызовы остальных функций. Создать функцию count_calls и
    global calls  # изменять в ней значение переменной calls. Эта функция должна
    calls += 1  # вызываться в остальных двух функциях.


def string_info(string=str(
    input('введите слово: _ '))):  # принимает аргумент - строку и возвращает кортеж из: длины этой строки,
    # строку в верхнем регистре, строку в нижнем регистре. Создать функцию
    tuple_ = (len(string), string.upper(),
              string.lower())  # string_info с параметром string и реализовать логику работы по описанию.
    print(tuple_)
    count_calls()  # Эта функция должна вызываться в остальных двух функциях.
    return tuple_


def is_contains(string_1=str(input('введите слово:_ ')), list_=list(input('введите список:_ '))): #  '''принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN/ Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.'''
    string_1 = str(string_1.upper())
    list_ = list(list_) #'''list_1 = [x.upper() for x in list_]  # перевод элементов списка в другой регистр с помощью генератора (дольше,чем map) 2,3784 print(timeit.timeit(lambda: [x.upper() for x in list_]),'скорость выполнения [x.upper() for x in list_]')'''
    list_ = list(map(str.upper, list_)) #''' перевод элементов списка в другой регистр с помощью map 2,1950'''
                                        # print(timeit.timeit(lambda: list(map(str.upper, list_))),'скорость выполнения list(map(str.upper, list_))')
    count_calls()                       # Эта функция должна вызываться в остальных двух функциях.
    for i in range(len(list_)):
        if list_ == string_1:
            result = True
            break
        else:
            result = False
            continue

    return result

print(string)
print(string_1)
print(list_)

string_info()
is_contains()
print(calls)



#print("12" in food) # команда in проверяет есть ли указанный пункт в списке

'''print(count_calls(),string_info())'''