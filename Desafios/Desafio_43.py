'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC).
Mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
'''

nome = input('Qual o seu nome? ')
peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura em ? (m) '))

imc = (peso / (altura**2))
print('O seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Seu IMC é classificado como Magreza!')

elif imc > 18.6 and imc < 24.9:
    print('Seu IMC é classificado como Saudável!')

elif imc > 25 and imc < 29.9:
    print('Seu IMC é classificado como Sobrepeso!')

elif imc > 30 and imc < 34.9:
    print('Seu IMC é classificado como Obesidade Grau I !')

elif imc > 35 and imc < 39.9:
    print('Seu IMC é classificado como Obsedidade Severa Grau I ! ! !')

else:
    print('Seu IMC é classificado como Obsidade Mórbida Grau III ! ! !')
