'''list_ = ['one', 'two','three']
for i in range(len(list_)):
    print(list_[i])'''
''''''     #  ЧЁТНОСТЬ В ЦИКЛЕ И СПИСКАХ !!!list_ = ['one', "huhu", 'two', 'three', ")()("]
'''list_ = ['one', "huhu", 'two', 'three', ")()("]
for i in range(len(list_)):  # счетчик с 0 !!!
    # if i % 2 == 0:    тк с 0 отсчёт, то наоборот надо сделать!!!
    if i % 2 != 0:
        list_[i] = " (:0) "
print(list_)'''
'''list_ = [2, 3, 4, 5, 1]
sum_ = 0 
for i in range(len(list_)):  # счетчик с 0 !!!
    sum_ += list_[i]
    print(sum_)''' # суммирование в цикле, #необходима переменная вне цикла (sum_)
'''for i in range(11 ):  # начиная с 0го индекса (по умолчанию) по 10ый, с шагом =1 (по умолчанию)
    for j in range(11):
        print(f'{i} * {j} = {i * j}')'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
pr = []
n_pr = []
numbers.remove(1)
print(numbers)
for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            n_pr.append(i)
            break
    else:
            pr.append(i)
print("n_pr",n_pr)
print("pr",pr)
