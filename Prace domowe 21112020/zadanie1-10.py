x = int(input("Podaj pozycję x: "))
y = int(input("Podaj pozycję y: "))

if 0 > x or x > 100 or 0 > y or y > 100:
    print("Jesteś poza planszą")
elif 0 <= x <= 10:
    if 10 <= y <= 90:
        print("Jesteś przy lewym boku")
    elif 0 <= y <= 10:
        print("Jesteś w lewym dolnym rogu")
    elif 90 <= y <= 100:
        print("Jesteś w lewym górnym rogu")
elif 90 <= x <= 100:
    if 10 <= y <= 90:
        print("Jesteś przy prawym boku")
    elif 0 <= y <= 10:
        print("Jesteś w prawym dolnym rogu")
    elif 90 <= y <= 100:
        print("Jesteś w prawym górnym rogu")
elif 10 < x < 90:
    if 90 <= y <= 100:
        print("Jesteś przy górnym boku")
    elif 0 <= y <= 10:
        print("Jesteś przy dolnym boku")
    else:
        print("Jesteś w centrum")