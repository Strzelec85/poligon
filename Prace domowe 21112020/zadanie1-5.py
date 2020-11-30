import math

a = float(input("Podaj długośćboku a: "))
b = float(input("Podaj długośćboku b: "))
c = float(input("Podaj długośćboku c: "))

if a + b > c and a + c > b and b + c > a:
    p = (a+b+c)/2
    pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
    pole = round(pole,2)
    print(f"Pole trójkąta równa się: {pole}")
else:
    print("To nie jest trójkąt")
    exit()
