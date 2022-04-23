'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros
'''
print('=-'*20)
print('{:=^40}'.format(' SIMULADOR DE PAGAMENTOS '))
print('=-'*20)


produto = float(input('\nQual o valor do produto? R$ '))

produto_din = produto - (produto * .10)
produto_cartao_avista = produto - (produto * .05)
produto_2x_cartao = produto / 2


print('\nEscolha a opção de pagamento:\n\n[ 1 ] Pagamento à vista dinheiro ou cheque (10% de desconto).\n[ 2 ] Pagamento à vista no cartão (5% de desconto)\n[ 3 ] Pagamento em até 2x no cartão (Preço normal)\n[ 4 ] Pagamento em 3x ou mais no cartão (20% de Juros)')

escolha = int(input('\nQual sua escolha? '))

if escolha == 1:
    print('O valor do produto no dinheiro ou cheque ficará: R$ {:.2f}'.format(produto_din))

elif escolha == 2:
    print('O valor do produto no cartão à vista ficará: R$ {:.2f}'.format(produto_cartao_avista))

elif escolha == 3:
    print('O valor do produto em até 2x no cartão ficará: 2 parcelas de R$ {:.2f}'.format(produto_2x_cartao))

elif escolha == 4:
    parcela = int(input('Em quantas vezes deseja parcelar? '))
    produto_3x_cartao = (produto + (produto * .20)) / parcela
    print('O valor do produto em {}x no cartão ficará:\n{} parcelas de R$ {:.2f}'.format(parcela, parcela, produto_3x_cartao))

elif escolha != 1 and escolha != 2 or escolha != 3 or escolha != 4:
    print('Escolha uma opção válida!!')

