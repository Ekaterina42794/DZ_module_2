print('Задание "Раз, два, три, четыре, пять .... Это не всё?":')
'''Примечания (рекомендации):
Весь подсчёт должен выполняться одним вызовом функции.
Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.

Т.к. каждая структура может содержать в себе ещё несколько элементов,
можно использовать параметр *args

Для определения типа данного используйте функцию isinstance.

Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99'''

'''Входные данные (применение функции):
 data_structure = [
                    [1, 2, 3],
                    {'a': 4, 'b': 5},
                    (6, 
                       {'cube': 7, 'drum': 8}),
                    "Hello",
                    ((),
                        [
                         {
                           (
                             2,
                             'Urban',
                             ('Urban2', 35)
                                            )
                                                }
                                                 ]
                                                  )
                                                    ]

result = calculate_structure_sum(data_structure)
print(result)


Выходные данные (консоль):
99'''


def calculate_structure_sum(data_structure):
    s = 0
    if isinstance(data_structure, (int, float)):
        s += data_structure
    elif isinstance(data_structure, str):
        s += len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            s += calculate_structure_sum(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            s += calculate_structure_sum(key)
            s += calculate_structure_sum(value)
    return s


data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),"Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)
# result= calculate_structure_sum((1,'vfvfv'))
# print(result)
# result = calculate_structure_sum((1, 'vfvfv', ['bnb', {"a": 7}], (1, 2, 3)))
# print(result)


#_________________________________________________________________

#print(help(isinstance))
''' Помощь по встроенной функции isinstance в модулях builtins:
isinstance(obj, class_or_tuple, /)
Возвращает, является ли объект экземпляром класса или его подкласса.

Кортеж, как в ``isinstance(x, (A, B, ...))``, может быть указан в качестве цели для проверки. 
Это эквивалентно ``isinstance(x, A) или isinstance(x, B) или ...`` и т. д.'''

#print(help(data_structure))
'''class list(object)
| list(iterable=(), /)
|
| Встроенная изменяемая последовательность.|
| Если аргумент не указан, конструктор создает новый пустой список.
| Аргумент должен быть итерируемым, если указан.
|
| Методы, определенные здесь:
|| __add__(self, value, /)
| Возврат self+value.
|
| __contains__(self, key, /)
| Возврат bool(key in self).
|
| __delitem__(self, key, /)
| Удалить self[key].
|
| __eq__(self, value, /)
| Возврат self==value.
|
| __ge__(self, value, /)
| Возврат self>=value.
|
| __getattribute__(self, name, /)
| Возврат getattr(self, name).
|
| __getitem__(self, index, /)
| Возвращает self[index].
|
| __gt__(self, value, /)
| Возвращает self>value.
|
| __iadd__(self, value, /)
| Реализует self+=value.
|
| __imul__(self, value, /)
| Реализует self*=value.
|
| __init__(self, /, *args, **kwargs)
| Инициализирует self. См. help(type(self)) для точной сигнатуры.
|
| __iter__(self, /)
| Реализует iter(self).
|
| __le__(self, value, /)
| Возвращает self<=value.
|
| __len__(self, /)
| Возвращает len(self).
|
| __lt__(self, value, /)
| Возвращает self<value.
|
| __mul__(self, value, /)
| Возвращает self*value.
|
| __ne__(self, value, /)
| Возвращает self!=value.
|
| __repr__(self, /)
| Возвращает repr(self).
|
| __reversed__(self, /)
| Возвращает обратный итератор по списку.
|
| __rmul__(self, value, /)
| Возвращает value*self.
|
| __setitem__(self, key, value, /)
| Устанавливает self[key] в значение.
|
| __sizeof__(self, /)
| Возвращает размер списка в памяти в байтах.
|
| append(self, object, /)
| Добавить объект в конец списка.
|
| clear(self, /)
| Удалить все элементы из списка.
|
| copy(self, /)
| Верните поверхностную копию списка.
|
| count(self, value, /)
| Верните количество вхождений значения.
|
| extend(self, iterable, /)
| Расширьте список, добавив элементы из итерируемого объекта.
|
| index(self, value, start=0, stop=9223372036854775807, /)
| Верните первый индекс значения.
|
| Вызывает ValueError, если значение отсутствует.
|
| insert(self, index, object, /)
| Вставьте объект перед индексом.
|
| pop(self, index=-1, /)
| Удалите и верните элемент с индексом (по умолчанию последний).
|
| Вызывает IndexError, если список пуст или индекс выходит за пределы диапазона.
|
| remove(self, value, /)
| Удалите первое вхождение значения.
|
| Вызывает ValueError, если значение отсутствует.
|
| reverse(self, /)
| Обратный порядок *НА МЕСТЕ*.
|
| sort(self, /, *, key=None, reverse=False)
| Сортирует список в порядке возрастания и возвращает None.
|
| Сортировка выполняется на месте (т. е. сам список изменяется) и стабильна (т. е.
| порядок двух равных элементов сохраняется).
|
| Если задана ключевая функция, примените ее один раз к каждому элементу списка и отсортируйте их по возрастанию или убыванию в соответствии со значениями их функций.
|
| Флаг обратного порядка можно установить для сортировки по убыванию.
|
| ----------------------------------------------------------------------
| Методы класса, определенные здесь:
|
| __class_getitem__(...)
| См. PEP 585
|
| ----------------------------------------------------------------------
| Статические методы, определенные здесь:
|
| __new__(*args, **kwargs)
| Создает и возвращает новый объект. Точную сигнатуру см. в help(type).
|
| ----------------------------------------------------------------------
| Данные и другие атрибуты определены здесь:
|
| __hash__ = None

None'''