# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('-='*15)
print('   Mostrador de número pares')
print('-='*15)

for pares in range(0,51,2):
    print(pares, end=' ')

print('Acabou!!')

''' 
Outro modo .. dividindo por 2 com resto 0, pois sabemos que são número pares!

for pares in range(1,51):
    if pares % 2 == 0: #Para saber se o número é par absoluto. Porém, o número de repetições é maior.
        print(pares, end=' ')

'''