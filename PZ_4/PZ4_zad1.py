#Даны два целых числа A и B (A < B). Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B), а также количество N этих чисел.
a = input("Введите первое число а: ")
while type (a) != int:
    try:
        a = int(a)
    except ValueError:
        print("неверно")
        a = input("Введите первое число а: ")
b = input("Введите второе число b: ")
while True:
    try:
        b = int(b)
        if b > a:
            break
        else:
            print("Ошибка: число а должно быть меньше b")
            b = input("Введите число b заново: ")
    except ValueError:
        print("неверно")
        b = input("Введите число b заново: ")
k = 0
print("числа в порядке возрастания:")
while a <= b:
    print(a)
    a += 1
    k += 1
print("Количество чисел N:", k)