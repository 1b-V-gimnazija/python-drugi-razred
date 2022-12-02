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

# Unosimo dva broja između kojih provjeravamo količinu prostih brojeva te brojač koliko prostih brojeva ima.
prviBroj = int(input("Prvi Broj: "))
drugiBroj = int(input("Drugi Broj: "))
counter = 0

# Definiramo for petlju od prvog i uključujući drugi broj.
for i in range (prviBroj, drugiBroj+1):
    # Pokrećemo funkciju sa brojem i koja provjerava je li broj prost.
    if prostBroj(i):
        # Ako je broj prost, dodajemo na brojač.
        counter += 1

# Ispisujemo brojač.
print(counter)