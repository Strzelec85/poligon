wzrost = float(input("Podaj wzrost w cm: "))
waga = int(input("Podaj wagę w kg: "))

bmi = round(waga / (wzrost/100)**2,2)

print(f"Twoje BMI: {bmi}")

if bmi <= 18.5:
    print("Masz niedowagę")
elif 18.5 < bmi < 25:
    print("Masz normalną wagę")
elif 25 <= bmi < 30:
    print("Masz nadwagę")
else:
    print("Masz otyłość")