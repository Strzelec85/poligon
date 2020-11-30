
tablica = [49, 50, 20, 40, 35, 10]

#Wersja A
print(tablica)
minim = None
maxim = None
indeks_min = None
indeks_max = None

for i in range(0, len(tablica)):
    if minim == None and maxim == None:
        minim = tablica[i]
        maxim = tablica[i]
    if minim > tablica[i]:
        minim = tablica[i]
        indeks_min = i
    if maxim < tablica[i]:
        maxim = tablica[i]
        indeks_max = i

tablica[indeks_max] = minim
tablica[indeks_min] = maxim
print(tablica)
print()
#Wersja B
tablica = [49, 50, 20, 40, 35, 10]
print(tablica)
maksimum_i = tablica.index(max(tablica))
minimum_i = tablica.index(min(tablica))

robocza = tablica[maksimum_i]
tablica[maksimum_i] = tablica[minimum_i]
tablica[minimum_i] = robocza

print(tablica)