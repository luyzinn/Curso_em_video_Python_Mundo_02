'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''

from datetime import date
from time import sleep

atleta = input('\nInsira o nome do atleta: ')
ano_nascimento = int(input('\nQual o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print('\nVoce tem {} anos! Entao:  '.format(idade))

if idade <= 9:
    print('\nSua categoria é MIRIM')

elif idade > 9 and idade <= 14:
    print('\nSua categoria é INFANTIL')

elif idade > 14 and idade <= 19:
    print('\nSua categoria é JÚNIOR')

elif idade > 19 and idade <= 25:
    print('\nSua categoria é SENIOR')

else:
    print('\nSua categoria é MASTER')
