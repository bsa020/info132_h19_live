nok_amount = int(input("Antall kroner?\n"))
nok_to_eur = 0.100187
nok_to_usd = 0.110449
eur_amount = nok_amount * nok_to_eur
usd_amount = nok_amount * nok_to_usd

# print(nok_amount, "kroner tilsvarer", eur_amount, "Euro og", usd_amount, "Dollar")
eur_sign = u'\N{euro sign}'
usd_sign = u'\N{dollar sign}'

print(f"{nok_amount} kroner tilsvarer {eur_amount:.2f}{eur_sign} og {round(usd_amount, 2)}{usd_sign}")


# If (and/or), elif, else
x = 8

if x > 5:
    if x > 7:
        print("x er over 5 og 7")

if x > 5 and x > 7:
    print("x er over 5 og 7")


# Try / except (unntakshåndtering)
while True:
    antall_kroner = int(input("Velg et tall mellom 1 og 10\n"))
    if antall_kroner not in range(1,11):
        print("Feil! Du må velge mellom 1 og 10")
        continue
    break
     

print(antall_kroner)
