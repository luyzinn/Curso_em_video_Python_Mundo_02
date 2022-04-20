# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# 1 - Se ele ainda vai se alistar ao serviço militar
# 2 - Se é a hora exata de se alistar 
# 3 - Se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date

nascimento = int(input('Qual o ano do seu nascimento? (Ex. 1989): '))

ano_atual = date.today().year
idade = ano_atual - nascimento

if idade == 18:
    print('Você tem {} anos! Essa é a idade certa para fazer o alistamento!!'.format(idade))

elif idade > 18:
    print('Você já deveria ter se alistado..\nNas verdade já se passaram {} anos do seu alistamento que foi em {}!!'.format(idade - 18,nascimento + 18))

elif idade < 18:
    print('Você ainda esta novo .. \nNa verdade faltam {} anos para fazer o alistamento que será em {}!!'.format(18 - idade, nascimento + 18))




