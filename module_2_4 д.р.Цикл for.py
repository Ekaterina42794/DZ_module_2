'''Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
Цель: закрепить навык решения задач при помощи цикла for, применив знания об основных типах данных.

Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
Пункты задачи:
Создайте пустые списки primes и not_primes.
При помощи цикла for переберите список numbers.
Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
Выведите списки primes и not_primes на экран(в консоль).

Пример результата выполнения программы:
Исходный код:
 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Вывод на консоль:
Primes: [2, 3, 5, 7, 11, 13]
Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
Примечания:
Учтите, что число 1 не является ни простым, ни составным числом, поэтому оно отсутствует в конечных списках.
Для проверки на простоту числа вам нужно убедиться, что выбранное число не делиться ни на что в диапазоне от 2 до этого числа(не включительно).
Попробуйте оптимизировать(ускорить) процесс выяснения простоты числа при помощи оператора break, когда найдёте делитель. (Не обязательно)
Переменные меняющее своё булевое состояние на противоположное в процессе проверки, как is_prime, в кругах разработчиков называются перменными-флагами(flag).'''

'''простое число - целое число >0 , исключая 1, делится на 1 и на себя'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(numbers)
numbers.remove(1)
print(numbers)
# создаем пустой список для хранения простых чисел
primes = []
not_primes = []
# пробегаем все числа от 2 до N
for i in numbers:  # пробегаем все числа от 2 до текущего
    for d in range(2, i - 1):
        if i % d == 0:
            not_primes.append(i)
            break
    else:
        primes.append(i)

print("простые", primes)
print("Не простые", not_primes)
