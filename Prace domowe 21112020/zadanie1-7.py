towar = input("Co chcesz kupić? ")
cena = float(input("Podaj cenę towaru: "))
ilosc = float(input("Podaj ilość towaru: "))

print(f"Za {towar}, który chcesz kupić, zapłacisz {round(cena * ilosc,2)} zł.")