# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

print("-=" * 20)
print("       SIMULADOR DE EMPRÉSTIMO       ")
print("-=" * 20)
print(" ")

valor_casa = float(input("Qual o valor da casa? R$ "))
salario_comprador = float(input("Qual o valor do salário do comprador? R$ "))
tempo_financiamento = int(input("Em quantos anos pretende financiar o imóvel? "))

tempo_financiamento_meses = tempo_financiamento * 12 #transformando anos em meses

prestacao = valor_casa / tempo_financiamento_meses
percentual_salario = salario_comprador * 0.3

if prestacao < percentual_salario:
    print(" ")
    print("PROCESSANDO .. ")
    sleep(2)
    print("... ")
    sleep(2)
    print("Voce está ápito para prosseguir com o financiamento")
    print(" ")
    print("O tempo de financiamento é de {} meses e o valor da prestaçao é de R$ {:.2f}.".format(tempo_financiamento_meses, prestacao))
    print(" ")
elif prestacao > percentual_salario:
    print("PROCESSANDO .. ")
    sleep(2)
    print("... ")
    sleep(2)
    print("Voce NAO está ápito para prosseguir com o financiamento")
    print(" ")
    print("O valor da sua prestaçao (R$ {:.2f}) é maior que 30% (R$ {:.2f}) do seu salário de R$ {:.2f}".format(prestacao,percentual_salario, salario_comprador))
    print(" ")
    print("O tempo de financiamento é de {} e o valor da prestaçao é de {:.2f}".format(tempo_financiamento_meses, prestacao))
    print(" ")