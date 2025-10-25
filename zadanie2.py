# Zadanie 2
# Napisz program porządkowania trzech liczb x, y i z. Od najmniejszej do największej, bez użycia
# wbudowanych funkcji

x = input("Podaj 1 liczbę: ")
y = input("Podaj 2 liczbę: ")
z = input("Podaj 3 liczbę: ")

if x > y:
    x, y = y, x
if x > z:
    x, z = z,x
if y > z:
    y, z = z,y
print("Posortowane liczby: ", x,y,z)