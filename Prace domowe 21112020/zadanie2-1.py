from random import randint

x = randint(0, 99)
y = randint(0, 99)
suma = x + y

odp = int(input(f"Wylosowane liczby to {x} oraz {y}, podaj ich sumę: "))

while True:
    if odp == suma:
        print("Zgadłeś")
        break
    else:
        print("Źle, jeszcze raz")
        odp = int(input("Podaj sumę "))