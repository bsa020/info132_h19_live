# If-setninger

word = "heisann"

if word in ("hei", "hallo", "heisann"):
    print("Ordet er hei eller hallo")

x = 200

if x < 40:
    if x < 90:
        if x < 80:
            print("x er mindre enn 80")
        if x > 60:
            print("x er større enn 60")
        if x == 40:
            print("x er akkurat 40")
if x < 50:
    print("x er mindre enn 50 (if)")
else:
    print("else-setning")



# Exceptions (try/except)



try:
    # prøv å gjøre det som står her
    print(variabelnavn)
except NameError:
    # hvis noe går galt, gjør dette i stedet
    print("Beklager, du brukte en variabel som ikke finnes.")

import random

spmtegn = "?" * random.randint(20,40)
print(spmtegn)
svar = len(spmtegn)

try:
    gjetning = int(input("Hvor mange spørsmålstegn?"))
except ValueError:
    print("Du tastet en ugyldig verdi. Skriv kun et heltall mellom 20 og 40.")
    gjetning = int(input("Hvor mange spørsmålstegn?"))

resultat = (svar == gjetning)
print(f"That's {resultat}")

if svar == gjetning:
    print("That's True")
elif svar != gjetning:
    print("That's False")


nok_amount = int(input("Hvor mange kroner?\n"))
nok_to_eur = 0.100120
nok_to_usd = 0.110300
eur_amount = round(nok_amount * nok_to_eur, 2)
usd_amount = round(nok_amount * nok_to_usd, 2)

eur_sign = u'\N{euro sign}'
usd_sign = u"\N{dollar sign}"

# Med forklarende variabelnavn
print(f"{nok_amount} kroner tilsvarer {eur_amount:.2f}{eur_sign} og {usd_amount}{usd_sign}")

# Med generiske variabelnavn
x, y, sign1, sign2 = None, None, None, None
print(f"{x} kroner tilsvarer {y:.2f}{sign1} og {z}{sign2}")


# %-formatering
# .format()
# f-string

print("Bjørn\nHelge\nSandblåst")
print("Bjørn", "Helge", "Sandblåst", sep="\n")

first_name = "Bjørn"
middle_name = "Helge"
last_name = "Sandblåst"

print(first_name, middle_name, last_name, sep="\n")
