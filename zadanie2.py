# Zadanie 2
# Napisz program porządkowania trzech liczb x, y i z. Od najmniejszej do największej, bez użycia
# wbudowanych funkcji

x = int(input("Podaj 1 liczbę: "))
y = int(input("Podaj 2 liczbę: "))
z = int(input("Podaj 3 liczbę: "))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print("Liczby od najmniejszej do największej:", x, y, z)
