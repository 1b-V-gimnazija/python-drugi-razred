# Unosimo rečenicu te inicializiramo varijablu koja će nam držati mjesto zadnjeg ispisa.
sentence = str(input())
lastStop = 0

# Vrtimo petlju koja je jednaka dužini stringa
for i in range(len(sentence)):
    if sentence[i] == " ":
        # Ako naiđemo na razmak, ispisujemo sve znakove od zadnje rječi do kraja trenutne riječi.
        print(sentence[lastStop:i].capitalize())
        # Na kraju mjenjamo varijablu zadnjeg ispisa.
        lastStop = i + 1