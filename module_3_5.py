print('Задача "Рекурсивное умножение цифр": ',
      'Функция, которая принимает аргумент целое ',
      'число number и подсчитывает произведение цифр этого числа.',sep='\n')
print('')


def get_multiplied_digits(number):
    # которая принимает аргумент целое число number
    # и подсчитывает произведение цифр этого числа.
    str_number = str(number)
    # Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    if len(str_number) > 1:
        first = int(str_number[0])
        # Основной задачей  будет отделение первой цифры в числе:
        # создайте переменную first и запишите  в неё первый символ из str_number
        # в числовом представлении(int).
        return first * get_multiplied_digits(int(str_number[1:]))
        # Таким образом вы умножите первую цифру числа на результат работы этой же
        # функции с числом,но уже без первой цифры. пункт можно выполнить только тогда,
        # когда длина str_number больше 1,иначе  не получиться взять срез str_number[1:].
    else:
        return number
        # Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first


print(get_multiplied_digits(5546547))
print(get_multiplied_digits(512))