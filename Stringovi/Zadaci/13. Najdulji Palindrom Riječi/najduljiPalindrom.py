# Unosimo riječ
word = str(input("Unesite rijeČ: "))
# Pripremamo varijablu za najdužu riječ.
longest = ""

# Pokrećemo prvu for petlju koja će ići od nule do duljine riječi
for i in range(0, len(word)):
    # Druga for petlja kreće od "i + 1" (zato što će nam prvi znak stringa uvijek biti i) te ide do kraja riječi.
    for j in range(i + 1, len(word) + 1):
        # Varijabla "substring" je interval od početka riječi, do njenog kraja.
        substring = word[i:j]
        # Ovdje provjeravamo je li riječ palindrom te je li duža od trenutačno najdulje spremljenog palindroma.
        if substring == substring[::-1] and len(substring) > len(longest):
            # Spremamo najdulji trenutačni palindrom u varijablu.
            longest = substring

# Ispisujemo najduži palindrom u riječi.
print(longest)