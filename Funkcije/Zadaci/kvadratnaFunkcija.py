# Kvadratna funkcija oblika f(x) = ax^2+bx+c. Iz ove funkcije možemo dobiti pravac koji sječe
# x-os u točkama koje se zovu nultokčke. Naš zadatak je vratiti True ako ima REALNE nultočke i False
# ako nema. Sad, pošto to nismo radili (još) iz matematike, ovaj zadatak se svodi na provjeru da je
# izraz b^2-4ac veći ili jednak nuli.

# Definiramo funkciju sa koeficjentima a, b i c (f(x) = ax^2+bx+c.).
def realneNultocke(a, b, c):
    # Provjeravamo je li izraz veći ili jednak nuli te vraćamo True ili False
    if b^2 - 4 *a*c >= 0:
        return True
    else:
        return False

# Unosimo tri koeficijenta za provjeru.
a = int(input("Unesite prvi koeficijent: "))
b = int(input("Unesite drugi koeficijent: "))
c = int(input("Unesite treći koeficijent: "))

# Evauliramo te ispisujemo True ili False
print(realneNultocke(a, b, c))