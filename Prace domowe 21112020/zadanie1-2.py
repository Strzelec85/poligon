dni = {
    1: "podzieniałek",
    2: "wtorek",
    3: "środa",
    4: "czwartek",
    5: "piątek",
    6: "sobota",
    7: "niedziela"
}

dzien = int(input("Podaj dzień, w którym oddałeś buty: "))
print(f"Oddałeś buty w {dni[dzien]}")

naprawa = int(input("Jak długo potrwa naprawa?: "))

if dzien + naprawa > 7:
    print(f"Buty dostaniesz w {dni[(dzien + naprawa)%7]}")