# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
contador = 0
for impares in range(1,501):
    if impares % 3 == 0 and impares % 2 == 1:
        soma = soma + impares #Aqui ele soma os valores da variável cada vez que ela se repete.. acumulando
        contador = contador + 1 #Aqui ele conta a quantidade de vezes da repetição
print('A soma de todos os valores é {} e isso se repetiu {} vezes'.format(soma,contador))


# impares % 3 == 0 - Verifica se ele é multiplo de 3
# impares % 2 == 1 - Determinar que ele é ímpar
# Para um acumulador é usando uma variavel recebendo valor 0 e somando com a variável que recebe os valores!
# Para um contador é usando uma variável recebendo valor 0 e somando mais 1 dentro do laço de repetição!
# Pode se usar soma = soma + 1 ou soma += 1 / contador = contador + 1 ou contador += 1