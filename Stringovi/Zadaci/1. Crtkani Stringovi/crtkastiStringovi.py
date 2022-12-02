# Uvodimo novi string "word"
word = str(input("Upišite riječ: "))

# Vrtimo petlju onoliko puta koliko ima slova
for i in range(len(word)):
    # Ispisujemo riječ + crtica i specificiramo da želimo sve ispisati u jednom redu.
    print(word[i] + "-", end="")