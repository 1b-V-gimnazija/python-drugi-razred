# Definiramo funkciju "zbroj" koja uzima dva parametra, prvi i drugi broj koji mora zbrojiti.
def zbroj (prviBroj, drugiBroj):
    # Vraćamo zbroj brojeva. Varijable "prviBroj" i "drugiBroj" su LOKALNE varijable. To znači da su dostupne samo u funkciji!
    return prviBroj + drugiBroj 

# Unosimo dva broja
input1 = int(input("Upišite prvi broj: "))
input2 = int(input("Upišite drugi broj: "))

# Ispisujemo izvod funkcije, tako što ju pozivamo u printu: zbroj(input1, input 2). Pozivanjem se funkcija učita i kod se krene izvršavati
print(zbroj(input1, input2))

# Dolje definirane varijable se neće podudarati sa onima u funkciji jer su one lokalne samo toj funkciji.
prviBroj = 1
drugiBroj = 2

# Funkciju možemo iskoristiti više puta!
print(zbroj(prviBroj, drugiBroj))