# zad. 5
# a)
# Odczytaj podany plik notwania_gieldowe.txt zawierający dane dotyczące notowań kilku spółek.
# Wydrukuj każdą linię do konsoli
with open("notowania_gieldowe.txt") as plik:
    print(plik.read())

# b

with open("notowania_gieldowe.txt", "a") as plik:
    plik.write("\nALR, 113")
with open("notowania_gieldowe.txt", "r") as plik:
    print(plik.read())
