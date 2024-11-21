calls = 0  # Создать переменную вне функций.

def count_calls():  # подсчитывающая вызовы остальных функций. Создать функцию count_calls и
    global calls  # изменять в ней значение переменной calls. Эта функция должна
    calls += 1  # вызываться в остальных двух функциях.
    print(calls)
print(calls)

def string_info(string_):
    tuple_ = (len(string_), string_.upper(), string_.lower())
    print(tuple_)
    count_calls()  # Эта функция должна вызываться в остальных двух функциях.
    return tuple_





def is_contains(string_1=str(input('введите слово № 2:_ ')), list_[]):
    a = int(input("введите количество элементов списка: _ "))
    print(a)
    for i in range(a):
        if i-1<a:
        list_[i-1] = input("введите", i, "элемент списка")
        list_.append([])
    print(list_[])
    string_1 = str(string_1.upper())
    list_1 = list(map(str.upper, (list_1)))
# перевод элементов списка в другой регистр с помощью map
# print(timeit.timeit(lambda: list(map(str.upper, list_))))
    count_calls()  # Эта функция должна вызываться в остальных двух функциях.
    print(string_1)
    print(list_1)
    print(string_1 in list_1)
# count_calls()  # Эта функция должна вызываться в остальных двух функциях.
# print(result_)
    print(string_1 in list_1)
    return result_



string_info()
is_contains()
#count_calls()
print(calls)

