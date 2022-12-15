# Unosimo riječ te pripremamo string za najdužu riječ oblika xx.
word = str(input())
longest = ""

# Ovdje imamo dvije for petlje (čiji je cilj odrediti sve podstringove), prva će nam odrediti točku od koje krećemo
# a druga do koje dolazimo. Prva petja će ići od 0 do kraja riječi. Druga petlja će početi od mjesta desno od prve petlje,
# a završiti na kraju riječi. U drugu petlju stavljamo len + 1, zato što kada specificiramo interval u stringu, on neće uključivati
# desnu vrijednost, a mi želimo da je uključuje.
for i in range(0, len(word)):
    for j in range(i + 1, len(word) + 1):
        # Podstring spremamo u varijablu radi lakšeg korištenja.
        substring = word[i:j]
        # Znamo da će se podstring xx nalaziti u riječi samo ako je ona parne duljine (odonsno ako je možemo podijeliti po pola).
        if len(substring) % 2 == 0:
            # String dijelimo na dva dijela na sljedeći način:
            #   - Prvu polovicu stringa će mo dobiti tako da krenemo od početka (0) te da
            #   odemo do duljine stringa (apsolutno) podjeljeno s dva (ako je string 4 dug idemo od 0 do 2)
            #   - Drugu polovicu dobijemo tako da krenemo od prošle vrijednosti do kraja (len(substring)).
            firstHalf = substring[0:len(substring)//2]
            secondHalf = substring[len(substring)//2:len(substring)]

            # Ako su obije polovice jednake znači da imamo riječ u XX obliku (yay!), no samo moramo provjeriti je li to najduža
            # riječ koju smo za sad našli. Nezgodna stvar sa test primjerom "ananas" je to što u sebi ima dva podstringa oblika XX
            # koji su jednake duljine, zbog ove provjere duljine će program uvijek ispisati onu koja je prva došla.
            if firstHalf == secondHalf and len(longest) < len(substring):
                longest = substring

# Ovaj dio zadovoljava uvjet da program mora ispisati "Nema", ako nema traženog podstringa.
# ------------------------------------------------------------------------------------------------------
# EXTRA TIP: Jedna podla stvar koju možemo napraviti je staviti gornju petlju u funkciju te tu
# funkciju pokrenuti samo kada je dužina riječi parna te odmah ispisati "Nema" za riječi neparne duljine.
if len(longest) > 0:
    print(longest)
else:
    print("Nema")