#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('\033[mDigite um número inteiro: '))
total = 0

for primo in range(1, n+1):
        if n % primo == 0:
            print('\033[33m', end=' ')
            total = total + 1 
        else:
            print('\33[31m', end=' ')   
        print('{}'.format(primo), end='  ')

print('\n\033[mO número {} foi dividido {} vezes'.format(n, total))
if total == 2:
    print('\nO número {} é primo!'.format(n))
else:
    print('\nEsse número não é primo!!')
print(' ')