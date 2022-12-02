# Definiramo funkciju broj, sa parametrom "broj" kojeg moramo provjeriti.
def prostBroj(broj):
    # Na početku pretpostavljamo da je broj prost.
    isProst = True
    # Vrtimo for petlju od 2 do našeg broja (ne uključujući naš broj).
    for i in range(2, broj):
        # Ovdje prvojeravamo je li naš broj djeljiv sa bilo kim brojem do njega.
        if broj % i == 0:
            # Ako jest, varijabla isProst će biti False.
            isProst = False

    # Vraćamo varijablu koja će biti ili True, ako je broj prost ili False ako nije.
    return isProst

# Unosimo broj za provjeru.
zaProvjeriti = int(input("Unesite broj: "))

# Radimo for petlju od dva do broja za provjeru. Iako smo mogli staviti "i"
# varijablu za petlju, ovdje je stavljno "j" radi preglednosti.
for j in range(2, zaProvjeriti + 1):
    # Provjeravamo hoće li naša funkcija vratiti "True" te ako hoće ispisujemo taj prost broj.
    # Brza napomena da je ovaj if, isto kao da smo napisali "if prostBroj(j) == True", zato što će
    # pri pozivanju funkcije, ona vratiti ili True ili False.
    if prostBroj(j):
        print(j)
    
