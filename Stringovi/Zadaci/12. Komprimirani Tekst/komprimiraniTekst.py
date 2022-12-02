# Unosimo kompresiranu riječ.
compressedWord = str(input("Unesite komprimirani tekst: "))
# Pripiremamo varijablu za ne kompresiranu riječ.
uncompressedWord = ""

# Vrtimo for petlju koja kreće od nule te ide po riječi sa razlikom dva (2, 4, 6, 8...).
for i in range(0, len(compressedWord), 2):
    # Kako bi dekompresirali riječ neki znak X ćemo dodati T puta. Prvo ćemo pristupiti znaku, a zatim ga
    # pomnožiit onoliko puta koliko je broj iza tog znaka.
    uncompressedWord += compressedWord[i] * int(compressedWord[i + 1])

# Ispisujemo dekompresiranu riječ.
print(uncompressedWord)