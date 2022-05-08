# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

'''
Desafio 09:

n = int(input("Digite um valor inteiro: "))
print("A tabuada de {} é:".format(n))
print("{}  x {:2} = {:2}".format(n,1,n*1))
print("{}  x {:2} = {:2}".format(n,2,n*2))
print("{}  x {:2} = {:2}".format(n,3,n*3))
print("{}  x {:2} = {:2}".format(n,4,n*4))
print("{}  x {:2} = {:2}".format(n,5,n*5))
print("{}  x {:2} = {:2}".format(n,6,n*6))
print("{}  x {:2} = {:2}".format(n,7,n*7))
print("{}  x {:2} = {:2}".format(n,8,n*8))
print("{}  x {:2} = {:2}".format(n,9,n*9))
print("{}  x {:2} = {:2}".format(n,10,n*10))
'''

print('=-'*15)
print('   TABUADA DE MULTIPLICAÇÃO')
print('=-'*15)

'''n = int(input('\nDigite um valor para saber a tabuada: '))
contador = 0
acumulador = 0

print(' ')

for tabuada in range(1,11):
    contador = contador + 1
    resultado = n * contador
    print('{}  x {:2} = {:2}'.format(n, contador, resultado))'''

numero = int(input('Digite u número para ver a tabuada: '))
for tabuada in range(1,11):
    print('{}  x {:2} = {:2}'.format(numero,tabuada,numero*tabuada)) #Outra forma de fazer - Mais simples
    