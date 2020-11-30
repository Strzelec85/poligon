cenaz = float(input("Podaj cenę za kilogram ziemniaków: "))
print(f"Cena za kilogram ziemniaków: {cenaz} zł. Za 5 kg. ziemniaków należy zapłacić {5 * cenaz} zł.")

cenaz = float(input("Podaj cenę za kilogram ziemniaków: "))
iloscz = float(input("Podaj ile kilogramów chcesz kupić: "))
print(f"Cena za kilogram ziemniaków: {cenaz} zł. Za {iloscz} kg. ziemniaków należy zapłacić {iloscz * cenaz} zł.")

cenaz = float(input("Podaj cenę za kilogram ziemniaków: "))
iloscz = float(input("Podaj ile kilogramów chcesz kupić: "))
cenab = float(input("Podaj cenę za kilogram bananów: "))
iloscb = float(input("Podaj ile kilogramów bananów chcesz kupić: "))
kosztz = cenaz * iloscz
kosztb = cenab * iloscb
print(f"Za wszystko zapłacisz {kosztz + kosztb} zł.")

if (kosztb > kosztz):
    print("Więcej zapłacisz za banany")
elif (kosztz > kosztb):
    print("Więcej zapłacisz za ziemniaki")
else:
    print("Za oba produkty zapłacisz tyle samo")
