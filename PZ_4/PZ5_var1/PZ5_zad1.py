#Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
#результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
#получится нуль?
def count_steps(n):
    steps = 0
    while n > 0:
        s = 0
        temp = n
        while temp > 0:
            s = s + (temp % 10)
            temp = temp // 10
        n = n - s
        steps = steps + 1
    return steps
n = input("Введите целое число: ")
while True:
    try:
        n = int(n)
        if n > 0:
            break
        else:
            print("ошибка. число должно быть больше нуля")
    except ValueError:
        print("ошибка.")
    n = input("Введите заново: ")
print("Через", count_steps(n), "действий получится нуль")