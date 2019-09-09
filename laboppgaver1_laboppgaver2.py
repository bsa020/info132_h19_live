""" Live-gjennomgang av laboppgaver 1 """

import random
import math


print('************')
print('     *      ')
print('     *      ')
print('     *      ')
print('     *      ')
print('     *      ')


print('''
*********
    *
    *
    *
    *
''')

bokstav_t = ''' 
*********
    *
    *
    *
    *
'''

print(bokstav_t)

# Oppgave 2

# Rett svar, uten feil i syntaks/logikk/semantikk
antall_studenter = input("Hvor mange studenter er det?\n")
antall_studenter = int(antall_studenter)
antall_kvinner = int(input("Antall kvinner?"))
kvinneandel = antall_kvinner / antall_studenter
kvinneandel = round(kvinneandel, 2)
print(f'Kvinneandelen er {kvinneandel}')


# Oppgave 3

# Fahrenheit til celsius
grader_celsius = float(input('Grader celsius? '))
grader_fahrenheit = (grader_celsius * (9/5)) + 32
f_til_c = (grader_fahrenheit - 32) * (5/9)

# Uten avrunding
print(f'{grader_celsius} C er {grader_fahrenheit} F')
print(f'{grader_fahrenheit} F er {f_til_c} C')

# Tegnene kan også tas direkte i utskriften.
tegn_c = u"\N{degree celsius}"
tegn_f = u"\N{degree fahrenheit}"

# Med avrunding
print(f'{grader_celsius:.2f}{tegn_c} = {grader_fahrenheit:.2f}{tegn_f}')
print(f'{grader_fahrenheit:.2f}{tegn_f} = {f_til_c:.2f}{tegn_c}')

"""
Laboppgaver 2
"""

# Oppgave 2

n = int(input("Fra: "))
m = int(input("Til: "))
# Totalsum = 1 ... m, formel: (k*(k+1))/2
totalsum = (m*(m+1))/2
# Fratrekk 1 ... n-1
fratrekk = ((n-1)*n)/2
# Resultat = totalsum - fratrekk
resultat = totalsum - fratrekk

print(f'{n}+...+{m} = {int(resultat)}')

# Oppgave 3
antall = random.randint(1, 30)
spmtegn = antall * '?'
svar = len(spmtegn)
print(spmtegn)
gjetning = int(input("Guess the number of ?'s: "))
print(f"That's {svar == gjetning}")
print(f"The right answer is {svar}")

# Oppgave 4
n = input("1. siffer")
m = input("2. siffer")

nm = n+m
mn = m+n
nm_int = int(nm)
mn_int = int(mn)
kvadratrot = math.sqrt(nm_int*mn_int)
print(f'Kvadratroten av {nm}*{mn} = {kvadratrot}')















