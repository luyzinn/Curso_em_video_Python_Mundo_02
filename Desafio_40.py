'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
'''

print('=-' * 20)
print('           SISTEMA DE ALUNOS')
print('=-' * 20)

nome = input('Insira seu nome: ')
nota_1 = float(input('Insira sua primeira nota: '))
nota_2 = float(input('Insira sua segunda nota: '))
media = (nota_1 + nota_2) / 2

if media < 5.00:
    print('Sua média foi {:.2f}, inferior a 5.0 e por isso você esta  R E P R O V A D O  ! ! !'.format(media))

elif media > 5.00 and media < 6.9: 
    print('Sua média é {:.2f}, inferior a 7.0 .. mas há salvação .. você esta de  R E C U P E R A Ç Ã O  ! ! !'.format(media))

else:
    print('Parabéns! Sua média foi {:.2f}, você esta  A P R O V A D O ! ! !'.format(media))




