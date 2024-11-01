import random

result = []


def stone_1():
    n_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    win = random.choice(n_)
    return win


a = stone_1()
print("Для ", a)
for i in range(1, 20):
    if i < a:
        for j in range(1, 20):
            while j < a:
                y = i + j
                if stone_1() % y == 0:
                    result.append(j)
                continue
            else:
                result.remove(i)

print("пароль", result())
