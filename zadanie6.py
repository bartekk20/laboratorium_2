# Zad. 6 
# Napisz skrypt w Pythonie, który sprawdza, czy litera wprowadzona przez użytkownika jest duża czy mała

print("Program sprawdzjący czy podana litera przez użytkownika jest wielka lub mała")

litera = str(input("Podaj literę: "))

if litera.isupper():
    print("Litera jest wielka")
elif litera.islower():
    print("Litera jest mała")
else:
    print("Podaj literę!")
