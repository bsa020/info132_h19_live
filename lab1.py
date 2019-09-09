""" 
Gjennomgang lab 1 

Syntaks
    Skrivefeil = “alt” feil, koden kjører ikke
Datatyper
    Hva betyr string, int, boolean?
Variabler
    Holder verdier
    Bruk fornuftige navn!

Utskrift
    Ulike syntaks-alternativer (med samme resultat)
Funksjoner
    Innebygde og egne
    Kun innebygde funksjoner nå
    F.eks. print(), input(), int(), str()
Kommentering / dokumentasjon
    Lettere for andre å forstå koden
    Også lettere for deg selv, når du ser på kode du har skrevet for en stund siden
    Kan være til god hjelp for eksamen
"""

# Syntaks

first_name = "Bjørn Helge"
last_name  = "Sandblåst"

# print("Mitt navn er", first_name, last_name)
# print(first_name, last_name, "er seminarleder i INFO132")


string_var = 'Bjørn Helge'
int_var = 10  # heltall
float_var = int_var / 3
boolean_var = int_var > 10 # < og > er strengt mindre/større
# du kan også bruke <= og >=

# %-formatering
print("%s %s" % (first_name, last_name))
print("10 / 3 = %.2f" % float_var)
# .format
print("{} {}".format(first_name, last_name))
print("10 / 3 = {:.2f}".format(float_var))
# f-strings
print(f"{first_name} {last_name}")
print(f"10 / 3 = {float_var:.2f}")










