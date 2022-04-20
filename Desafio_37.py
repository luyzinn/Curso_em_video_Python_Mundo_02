# Escreva um programa em Python que leia um número inteiro qualquer 
# Peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('-=' * 20)
print('     Conversor de bases numéricas')
print('-=' * 20)

numero = int(input('Digite um número inteiro qualquer: '))
escolha = int(input('\nEscolha:\n[ 1 ] Para converter para Binário\n[ 2 ] Para converter para Octal\n[ 3 ] Para converter para Hexadecimal\n \nQual sua opção: '))

conversao_bin = bin(numero)
conversao_hex = hex(numero)
conversao_oct = oct(numero)

if escolha == 1:
    print('A conversão binária de {} é igual a {}'.format(numero,conversao_bin))

elif escolha == 2:
    print('A conversão octal de {} é igual a {}'.format(numero,conversao_oct))

elif escolha == 3:
    print('A conversão hexadecimal de {} é igual a {}'.format(numero,conversao_hex))

else:
    print('Opção inválida!! Tente novamente!')


