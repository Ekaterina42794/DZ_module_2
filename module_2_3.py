print('Нули ничто, отрицание недопустимо!')

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(my_list)
my_list.remove(0)
print(my_list)
index = 0
while index  < len(my_list):
    print(my_list[index])
    index += 1
    if my_list[index] < 0:
        print("цикл закончен",my_list[index],"<0")
        break