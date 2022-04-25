'''
Crie um programa que faça o computador jogar Jokenpô com você
Regras: 
O papel ganha da pedra porque a embrulha;
A tesoura ganha do papel porque o corta; 
A pedra ganha da tesoura porque a quebra
'''
from time import sleep
import random

print('=-'*20)
print('          Vamos jogar Jokenpô?')
print('=-'*20)

print('\nEu já escolhi minha jogada.. e você?')

'''
itens = ('Pedra', 'Papel', 'Tesoura')
escolha_pc = random.randint(0,2)

forma de fazer com uma lista de opções
'''

print('''Escolha qual será sua jogada:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura ''')

lista = ['Pedra', 'Papel', 'Tesoura']

escolha = int(input('\nQual sua escolha? '))
escolha_pc = random.choice(lista)

print('\nJ O')
sleep(1)
print('K E N')
sleep(1)
print('P Ô')
sleep(1)
   

if escolha == 1:
    print('-='*40)
    print('Hmm.. você escolheu Pedra .. eu escolhi .. {}'.format(escolha_pc))
    print('-='*40)
    if escolha == 1 and escolha_pc == 'Pedra':
        print('\nEscolhemos iguais .. ninguém ganhou!')
    elif escolha == 1 and escolha_pc == 'Papel':
        print('\nEu ganhei .. você perdeu ..ahuahua! ! ! ')
    elif escolha == 1 and escolha_pc == 'Tesoura':
        print('\nÉ .. eu perdi .. você ganhou! ! !')
elif escolha == 2:
    print('-='*40)
    print('Hmm.. você escolheu Papel .. eu escolhi .. {}'.format(escolha_pc))
    print('-='*40)
    if escolha == 2 and escolha_pc == 'Papel':
        print('\n Escolhemos iguais .. ninguém ganhou .. ')
    elif escolha == 2 and escolha_pc == 'Pedra':
        print('\n É.. eu perdi .. você ganhou .. de novo! ! !')
    elif escolha == 2 and escolha_pc == 'Tesoura':
        print('\nÉ .. Eu ganhei! Você Perdeu!! auhaua')
elif escolha == 3:
    print('-='*40)
    print('Hmm.. você escolheu Tesoura .. eu escolhi .. {}'.format(escolha_pc))
    print('-='*40)
    if escolha == 3 and escolha_pc == 'Tesoura':
        print('\nÉ .. escolhemos iguais de novo .. ninguém ganhou! ! !')
    elif escolha == 3 and escolha_pc == 'Papel':
        print('\nÉ .. Perdi de novo .. tá ruim hoje ..')
    elif escolha == 3 and escolha_pc == 'Pedra':
        print('\nEu ganhei de novo! Você perdeu! ! !')
else:
    print('-='*40)
    print('''\nATENÇÃO:\n\nEscolha entre Pedra [ 1 ], Papel [ 2 ] e Tesoura [ 3 ].. \nTente novamente!!!''')
    print('-='*40)


