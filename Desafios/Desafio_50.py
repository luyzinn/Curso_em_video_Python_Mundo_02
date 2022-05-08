# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
contador = 0
for par in range(1,7):
    numero = int(input('Digite o {}º número: '.format(par)))
    if numero % 2 == 0:
        soma = soma + numero 
        contador = contador + 1
        
print('Você digitou {} número pares.. A soma deles é igual a {}!'.format(contador,soma))
    

