# Funkcija za korjen koja će nam trebati poslije
from math import sqrt

# Definiramo funkciju sa parametrima koordinata i polumjera. Oprez za redoslijedom varijabli!
def sjekuSeKruznice(x1, x2, polumjer1, y1, y2, polumjer2):
    # Računamo udaljenost između dva središta. Ako je ta udaljenost veća nego zbroj polumjera, kružnice se ne sijeku.
    udaljenostSredišta = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    
    # Provjeravamo je li udaljenost središta veća od zbroja polumjera te vraćamo pripadajuće stringove za ispis.
    if polumjer1 + polumjer2 < udaljenostSredišta:
        return "Ne sijeku se"
    else:
        return "Sijeku se"

# Zbog toga što još ne znamo "split" funkciju, svaku varijablu zasebno unosimo.
prvaXKoordinata = int(input("Unesite prvu X koordinatu: "))
prvaYKoordinata = int(input("Unesite prvu Y kooridnatu: "))
prviPolumjer = int(input("Unesite prvi polumjer: "))
drugaXKoordinata = int(input("Unesite drugu X koordinatu: "))
drugaYKoordinata = int(input("Unesite drugu Y kooridnatu: "))
drugiPolumjer = int(input("Unesite drugi polumjer: "))

# Pokrećemo funkciju sa unesenim varijablma, na kraju će ona ispisati jedan od stringova. Oprez sa poretkom parametara!
print(sjekuSeKruznice(prvaXKoordinata, drugaXKoordinata, prviPolumjer, prvaYKoordinata, drugaYKoordinata, drugiPolumjer))