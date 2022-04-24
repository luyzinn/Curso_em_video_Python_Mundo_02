# Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, 
# que é uma estrutura versátil e simples de entender. 

'''for c in range(0,3,1):
    #n = input('Digite um número: ')
    print(c) #Lembrar da identação é fundamental'''


valor = int(input('Digite o primeiro valor da contagem: '))
valor_2 = int(input('Digite o ultimo valor da contagem: '))
passo = int(input('Digite o valor do passo:'))
for c in range(valor,valor_2,passo):
    print(c)

#Observações: Lembrar da identação é fundamental e dos dois pontos também.

