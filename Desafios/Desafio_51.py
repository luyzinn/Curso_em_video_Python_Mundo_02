# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('\nO primeiro termo da PA é {} e sua razão {}. Logo, os 10 primeiro termos da PA são:'.format(termo,razao))
print(termo, end=' ')

for repetir in range (1,10):
    termo = termo + razao
    print(termo,end=' ')
    