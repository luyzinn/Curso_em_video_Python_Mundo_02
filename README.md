# Curso em video - Python Mundo 02 (www.cursoemvideo.com)
*Repositório para os exercícios e desafios do curso de Python - Mundo 01 do Curso em Vídeo!!*

<h2> Anotações Importantes </h2><br/>

O Foco principal desse módulo sao as condiçoes e repetiçoes em python!

*Condicionais Aninhadas*

```
IF - SE
ELIF - SENAO SE
ELSE - SENAO
```

*Exemplo*
```
if soma > 0:
     print "Maior que Zero."
elif soma = 0:
     print "Igual a Zero."
else:
     print "Menor que Zero."
```


#### Operador Tipo Valor

```
==	Igualdade	Verifica a igualdade entre dois valores.
!=  	Igualdade  	Verifica a diferença entre dois valores.
> 	Comparação	Verificar se o valor A é maior que o valor B.
< 	Comparação	Verifica se o valor A é menor que o valor B.
>=	Comparação	Verifica se o valor A é maior ou igual ao valor B.
<=	Comparação	Verifica se o valor A é menor ou igual ao valor B.
In	Seqüência	Verifica se o valor A está contido em um conjunto.
```


### Estrutura de repetição FOR <br>

> Escrita no Python: for **C** in range (1,10)

for - Comando para repetições<br>
C - Variável de contagem.<br>
in - Comando para  inserir a contagem<br>
Range - Intervalo de contagem que vc quer que se repita
**Não esquecer dos :**
**Não esquecer da identação**

> **Exemplo:** for c in range (0,6)

Se desejar uma interação, ou definir um valor para os 'passos' ou 'pulos, usar maisum valor no final:

> **Exemplo:** for c in range(0,6,2)

Significa que vai fazer a contagem de 0 a 5 pulando de 2 em dois. 0 a 5 por que ele ignora o ultimo número.

> Em caso de contagem negativas: for c in range(7,0,-1)

Ele contou de 7 a 0 ..tirando um numero: 7,6,5,4,3,2,1

***Exemplo real:***<br>
```
valor = int(input('Digite o primeiro valor da contagem: '))<br>
valor_2 = int(input('Digite o ultimo valor da contagem: '))<br>
passo = int(input('Digite o valor do passo:'))<br>
for c in range(valor,valor_2,passo):<br>
print(c)<br>
```
> Verificação de pares e múltiplos: 
```
impares % 3 == 0 - Verifica se ele é multiplo de 3
impares % 2 == 1 - Determinar que ele é ímpar
```
> Detalhe para acumuladores e contadores:
```
Para um acumulador é usando uma variavel recebendo valor 0 e somando com a variável que recebe os valores!

Para um contador é usando uma variável recebendo valor 0 e somando mais 1 dentro do laço de repetição!

Pode se usar soma = soma + 1 ou soma += 1 / contador = contador + 1 ou contador += 1
```
    