# Unosimo broj setova i definiramo varijable za osvojene setove igrača A i B.
numberOfSets = int(input())
totalWonA = 0
totalWonB = 0

# Pokrećemo petlju koja će se vrtiti onoliko puta koliko imamo setova.
for i in range(numberOfSets):
    # Unosimo set te definiramo varijable za pobijede igrača A ili B unutar nekog seta.
    set = str(input())
    setWonA = 0
    setWonB = 0
    # Pokrećemo još jednu petlju koja se vrti onoliko puta koliko je dug set 
    for j in range (len(set)):
        # Ako je j-ti znak jednak A, dodajemo 1 u setWonA
        if set[j] == "A":
            setWonA += 1
        # Ako je j-ti znak jednak B, dodajemo 1 u setWonB
        elif set[j] == "B":
            setWonB += 1
    
    # Ako je u jednom setu više A, A je dobio jedan set, a u suprotnom B.
    if setWonA > setWonB:
        totalWonA += 1
    else:
        totalWonB += 1

# Ispisujemo rezultat u željenom obliku.
print(str(totalWonA) + " : " + str(totalWonB))
    
