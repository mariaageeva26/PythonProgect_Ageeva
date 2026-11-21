#Дан список A размера N и целые числа K и L (1 < K < L < N). Переставить в обратном
#порядке элементы списка, расположенные между элементами AK и AL, не включая
#эти элементы.

import random
N = int(input("Введите размер списка N: "))
K = int(input("Введите число К: "))
L = int(input("Введите число L: "))
a = []
for _ in range(N):
    a.append(random.randint(0, 99))
print("исходный список: ", a)
sredina = a[K + 1: L]
sredina.reverse()
a[K + 1 : L] = sredina
print("Измененный список:", a)