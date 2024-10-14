#Все ли равны?
print("Все ли равны?")
first_= input("Введите first:")
second_= input("Введите second:")
third_= input("Введите third:")
if first_== second_ and first_== third_:
    print("Вы ввели 3 одинаковых числа")
elif first_ == second_ or first_ == third_ or second_ == third_:
    print ("Вы ввели 2 одинаковых числа или числа разных типов")
else: print("Вы ввели разные числа или числа разных типов")