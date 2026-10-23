#Даны координаты точки, не лежащей на координатных осях OX и OY. Определить номер координатной четверти, в которой находится данная точка
while True:
    try:
        x = float(input("Введите х: "))
        y = float(input("Введите у: "))
        if x == 0 or y == 0:
            print("Ошибка, точка не должна лежать на координатных осях")
            continue
        if x > 0 and y > 0:
            q = 1
        elif x < 0 and y > 0:
            q = 2
        elif x < 0 and y < 0:
            q = 3
        elif x > 0 and y < 0:
            q = 4
        print(f"Точка находится в {q} координатной четверти.")
        break
    except ValueError:
        print("ошибка. Введите число")

