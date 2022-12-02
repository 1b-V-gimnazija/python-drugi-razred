# Unosimo ime.
name = str(input())
# Ispisujemo inicijale tako što uzimamo prvi znak u stringu te mu dodajemo točku i razamak,
# a inicijal prezimena ćemo naći odmah iza razmaka. Prema tome, korisitmo funkciju "find" koja će nam
# dati mjesto razmaka te njoj dodajemo jedan, kako bi dobili mjesto drugog inicijala. Na kraju dodamo točku.
print(name[0] + ". " + name[name.find(" ") + 1] + ".")