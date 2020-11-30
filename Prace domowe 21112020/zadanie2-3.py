ilosc = int(input("Ile liczb wprowadzasz? "))

liczby = []

licznik = 0

while licznik < ilosc:
    liczby.append(int(input(f"Podaj {licznik + 1} liczbę ")))
    licznik += 1

print(liczby)
suma = 0
min = None
max = None

for i in range(0, ilosc):
    suma += liczby[i]
    if min == None and max == None:
        min = liczby[i]
        max = liczby[i]
    if min > liczby[i]:
        min = liczby[i]
    if max < liczby[i]:
        max = liczby[i]

print(f"suma {suma}")
print(f"średnia {suma/ilosc}")
print(f"Minimum {min}")
print(f"Maksimum {max}")