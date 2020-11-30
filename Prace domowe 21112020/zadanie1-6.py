wiek = int(input("Podaj swój wiek: "))
ilosc = int(input("Ile biletów chcesz kupić? "))

if 0 <= wiek < 7:
    cena = 0
elif 7 <= wiek < 18:
    cena = 2.28
elif 18 <= wiek < 65:
    cena = 3.80
elif 65 <= wiek:
    cena = 1.90
else:
    print("Nieprawidłowy wiek")

naleznosc = ilosc * cena
print(f"Należność {naleznosc} zł")