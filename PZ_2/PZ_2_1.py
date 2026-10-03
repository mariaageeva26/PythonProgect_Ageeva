#Известно, что Х кг конфет стоит А рублей.Определить сколько стоит 1 кг и Y  этих же конфет.
while True:
    try:
        x=float(input("X кг: "))
        if x>0: break
    except ValueError:
        print("Неверное значение")

while True:
    try:
        a=float(input("A руб: "))
        if a>=0: break
    except ValueError:
        print("Неверное значение")

while True:
    try:
        y=float(input("Y кг: "))
        if y>=0: break
    except ValueError:
        print("Неверное значение")
print("1 кг:", a/x)
print(y, "кг:", a/x*y)