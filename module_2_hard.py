import random
def stone_1():
    n_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    win = random.choice(n_)
    return win
a = stone_1()
print("Для ", a)
result = []
for i in range(1, 20):
    if i < a:
        '''print("i=",i)'''
        for j in range(1, 20):
            if j < a:
                n=i+j
                if a % n == 0 and i<j:
                    result.append(i)
                    result.append(j)
                    '''print("j=", j)'''
                continue
print("пароль", result)
