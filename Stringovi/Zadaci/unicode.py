# Prvo uzimamo riječ i definiramo varijablu UNICODE mase.
word = str(input())
mass = 0

# Pokrećemo for petlju koja će nam se vrtiti onoliko puta koliko je string dug.
for i in range(len(word)):
    # Koristeći funkciju ord, na varijablu masa dodajemo "masu" znaka.
    # Funkcija ord će vratiti broj znaka X iz ASCII tablice.
    # NAPOMENA: ASCII i UNICODE tablica imaju jednakih prvih 256 znakova.
    mass += ord(word[i])

# Ispisujemo masu.
print(mass)