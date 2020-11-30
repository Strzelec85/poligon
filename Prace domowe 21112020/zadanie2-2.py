poziom = int(input("Podaj liczbę wierszy: "))

kolumny = 2 * poziom - 1

for w in range(1, poziom+1):
    for k in range(1, kolumny+1):
        if poziom - w < k < poziom + w:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()