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

# Pokrećemo funkciju i ispisujemo ili True ili False.
print(prostBroj(zaProvjeriti))
    
