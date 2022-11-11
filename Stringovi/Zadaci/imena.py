# Unosimo broj imena koje moramo provjeriti
numberOfNames = int(input("Upišite broj imena: "))
# Definiramo brojače za ženska i muška imena
women = 0
men = 0

# Vrtimo petlju onoliko puta koliko nam treba imena
for i in range(numberOfNames):
    # Unosimo ime
    name = str(input("Upišite ime: "))
    # Provjeravamo je li zadnje slovo u imenu a, ako je onda je ime žensko, a inače je muško.
    # Provjeru radimo tako što provjeravamo "duljina riječi - 1" slovo (len(abc) = 3, str[len(str) - 1] = c)
    if name[len(name) - 1] == "a":
        women += 1
    else:
        men += 1

# Ispisujemo broj muških i ženskih imena.
print("Muških: " + str(men) + "\n" + "Ženskih: " + str(women))