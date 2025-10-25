# Zad 7. Podana jest poniższa zmienna przechowująca ciąg znaków - hasło:
Hasło = 'pk47!jy0893'
dlugosc_hasla = len(Hasło)
znak = "!"

if dlugosc_hasla == 11 and znak in Hasło:
    print("Hasło jest poprawne")
else:
    print("Hasło jest błędne")
