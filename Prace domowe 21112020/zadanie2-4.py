from random import randint

liczba = randint(0,999)

odp = int(input(f"Wylosowana liczba to: "))
proba = 1
while True:
    if odp == liczba:
        print(f"Zgadłeś po {proba} próbach")
        break
    elif odp < liczba:
        print("Za mała")
        proba += 1
        odp = int(input("Jeszcze raz "))
    elif odp > liczba:
        print("Za duża")
        proba += 1
        odp = int(input("Jeszcze raz "))