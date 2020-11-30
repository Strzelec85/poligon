tekst = input("Podaj tekst: ")

licznik = 0

if tekst.find("<") == -1 or tekst.find(">ty") == -1:
    print("Brak nawiasu < >")
elif tekst.count("<") > 1 or tekst.count(">") > 1:
    print("Za dużo nawiasów")
else:
    licznik = tekst.find(">") - tekst.find("<") - 1

print(licznik)