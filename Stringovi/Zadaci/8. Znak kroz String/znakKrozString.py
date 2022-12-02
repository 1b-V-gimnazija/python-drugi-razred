# Unosimo riječ i znak
word = str(input())
character = str(input())

# Vrtimo petlju koje će se vrtiti onoliko puta koliko je duga riječ i jedan dalje, da dođemo do zadnjeg znaka
for i in range(len(word) + 1):
    # Kako bi ubacili slovo koristimo donji izraz.
    # Prvi dio će nam dati sva slova do i. Ako je i = 2, a riječ je ZNAK, vratit će nam ZN.
    # Zatim dodajemo znak te onda sa zadnjim dijelom pridodajemo sve znakove od i, do kraja riječi.
    print(word[:i] + character + word[i:])
    