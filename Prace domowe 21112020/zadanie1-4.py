wiek = int(input("Podaj swój wiek: "))
noce = int(input("Podaj ile nocy planujesz spędzić w hotelu: "))

if wiek < 18:
    koszt = noce * 100
else:
    if noce == 1:
        koszt = 200
    elif 1 < noce < 5:
        koszt = noce * 180
    else:
        koszt = noce * 150

if wiek >= 65:
    koszt = koszt - 0.1 * koszt

print(f"Zapłacisz: {koszt} zł.")
