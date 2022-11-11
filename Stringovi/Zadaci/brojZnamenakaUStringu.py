# Unosimo string simbola.
symbols = str(input())
# Definiramo brojač za količinu brojeva u stringu
numbers = 0

# Petlja koja se vrti onoliko puta koliko je string dug, tako da možemo provjeriti svaki znak.
for i in range(len(symbols)):
    # Koristeći metodu isnumeric() provjeravamo je li i-ti znak broj ili ne.
    # (Metoda isnumberic() će vratiti True ako string (jedan simbol ili više njih) je broj.)
    if symbols[i].isnumeric() == True:
        # Dodajemo jedan naše brojaču.
        numbers += 1

# Ispisujemo broj brojeva u stringu.
print(numbers)