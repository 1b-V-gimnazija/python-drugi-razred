# Unosimo neku riječ.
word = str(input("Unesite riječ: "))

# Koriteći "replace" metodu mjenjamo sve znakove iz tabilce sa X, pošto nas zanima samo duljina normalne riječi.
# Moramo zapamtiti da su stringovi "nonimmutable" (ne možemo ih mjenjati sa metodama), što znači da sve ove "replace-ove" moramo spremiti u novu varijablu.
count = word.replace("DZ=", "X").replace("D-", "X").replace("Z=", "X").replace("S=", "X").replace("C=", "X").replace("C-", "X").replace("LJ", "X").replace("NJ", "X")

# Ispisujemo duljinu riječi
print(len(count))