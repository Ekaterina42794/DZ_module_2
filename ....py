numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(numbers)
# создаем пустой список для хранения простых чисел
lst_ = []
lst_2 = []
# в k будем хранить количество делителей

# пробегаем все числа от 2 до N
for i in range(0, len(numbers)):
    # пробегаем все числа от 2 до текущего
    for j in [1,i]:
        # ищем количество делителей
        if i % j == 0:
            lst_.append(i)
    else:
        lst_2.append(i)
print(lst_)
print(lst_2)
