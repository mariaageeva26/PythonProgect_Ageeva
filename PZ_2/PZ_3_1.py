#Дано целое число А. Проверить истинность высказывания: "Число А является положительным".
A = input(print("Введите число А: "))
try:
    number = int(A)
    pol = number > 0
    print(pol)
except ValueError:
    print("ошибка. введите число")

