# Unosimo neku riječ.
word = str(input("Unesite riječ: "))
# Inicijaliziramo varijablu u kojoj ćemo imati riječ sa zamjenjenim znakovima.
switched = ""

# Ovu petlju koristimo za prebacivanje znakova, petlja kreće od nule, a ide do predzadnjeg znaka riječi.
# Zašto ne idemo do kraja riječi? Ako je riječ neparna, dobit ćemo "IndexError" kod stringova neparne duljine, odnosno 
# pokušat ćemo pristupit dio stringa koji ne postoji. Kako sad to? Zato što je treći parametar u
# for petlji "2", što znači da ćemo vrtiti petlju za dva razlike (2, 4, 6).
for i in range(0, len(word) - 1, 2):

    # Prebacit ćemo dva znaka tako što ćemo pristupiti i-tom + 1 znaku (npr. pRogramiranje) te
    # ćemo onda taj znak dodati prvog stringu "switched" (switched će biti: "r") te ćemo onda dodati
    # i-ti znak (Programiranje) stringu "switched" ("switched će biti "rp"). Tako ćemo prebaciti sve
    # znakove u stringu.
    switched += word[i + 1] + word[i]

# Ako je string neparne duljine, ne možemo prebaciti sve znakove (a pošto for petlja ne ide do kraja riječi)
# moramo na kraj dodati zadnje slovo unesene riječi.
if len(word) % 2 != 0:
    switched += word[len(word) - 1] 

# Ispisujemo riječ
print(switched)