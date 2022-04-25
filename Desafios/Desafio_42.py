'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
'''

print('-=' * 20)
print('     ANALISADOR DE TRIANGULO V2')
print('-=' * 20)

lado_1 = float(input('Qual a medida do primeiro lado do triangulo? '))
lado_2 = float(input('Qual a medida do segundo lado do triangulo? '))
lado_3 = float(input('Qual a medida do terceiro lado do triangulo? '))

cond_1 = (int(lado_2 - lado_3) < lado_1 < (lado_2 + lado_3)) == True
cond_2 = (int(lado_1 - lado_2) < lado_3 < (lado_1 + lado_2)) == True
cond_3 = (int(lado_1 - lado_3) < lado_2 < (lado_1 + lado_3)) == True

if cond_1 == cond_2 == cond_3:
    print('')
    print('Você pode formar um triângulo!!')

    if lado_1 != lado_2 != lado_3 != lado_1:
        print('')
        print('E ele é ESCALENO') 

    if lado_1 == lado_2 == lado_3:
        print('')
        print('E ele é EQUILÁTERO')

    if lado_1 == lado_2 != lado_3:
        print('')
        print('E ele é ISÓSCELES')

    if lado_1 != lado_2 == lado_3:
        print('')
        print('E ele é ISÓSCELES')
    
else:
    print('')
    print('Você não pode formar um triângulo!')