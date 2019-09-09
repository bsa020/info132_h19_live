'''
Vanlig praksis for navngivning av variabler
    Store/små bokstaver, “snake case”
    Ofte gode grunner - gir kode som er lettere å lese
Gjenbruk av variabler
    Bør/bør ikke? Når?
    Konvertering av datatype
    Eksempel: input()
Funksjoner
    Argumenter, returverdi
'''

x = 250 # antall kroner
y = 0.9 # Kurs NOK til EUR

# nok_amount = input("Hvor mange kroner? \n")
# nok_amount = float(nok_amount)
# print(nok_amount * 2)


# Eksempel på funksjon
def legg_sammen(x, y):
    resultat = x + y
    return resultat


ti_pluss_ti = legg_sammen(10,10)

print("Variabelen har verdi", ti_pluss_ti)

print(print("Hei"))





