#desaifo 28: Acertar um numero entre 0 e 5, usando o módulo random
from random import randint
num = int(input('tente acertar um número entre 0 e 5: '))
num_aleatorio = randint(0, 5)
if num == num_aleatorio:
    print('parabéns, você acertou!')
else:
    print(f'você errou, o número era {num_aleatorio}')

#desafio 29: ler a velocidade de um carro e mostrar se ele ultrapassou ou não o limite de velocidade, que é de 80 km/h. Se ele ultrapassou, mostrar quantos km/h ele estava acima do limite e mostrar a mensagem "MULTADO! Você deve pagar uma multa de R$ 7,00 por cada km/h acima do limite"
velocidade = float(input('qual é a velocidade do carro?; '))
if velocidade > 80:
    print('voce foi multado! voce deve pagar uma multa de {} rais'.format((velocidade - 80) * 7))
else:
    print('parabéns, você está dentro do limite de velocidade!')

#desafio 30: ler um número inteiro e mostrar se ele é par ou ímpar
num = int(input('digite um número inteiro: '))
if num % 2 == 0:
    print(f'o número {num} é par')
else:
    print(f'o número {num} é ímpar')

#desafio 31: preços de viagens
D = float(input('qual é a distância da viagem em km? '))
if D <= 200:
    print('o preço da passagem é R$ {:.2f}'.format(D * 0.50))
else:
    print('o preço da passagem é R$ {:.2f}'.format(D * 0.45))

#desafio 32: ler um ano e mostrar se ele é bissexto ou não
ano = int(input('digite um ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'o ano {ano} é bissexto')
else:
    print(f'o ano {ano} não é bissexto')

#desafio 33: ler três números e mostrar qual é o maior e qual é o menor
n1 = float(input('digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))
n3 = float(input('digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print(f'o maior número é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'o maior número é {n2}')
else:
    print(f'o maior número é {n3}')

#desafio 34: ler o salário de um funcionário e mostrar o novo salário, com um aumento de 15% para salários até R$ 1250,00 e um aumento de 10% para salários acima de R$ 1250,00
S = float(input('qual é o salário do funcionário? '))
if S <= 1250:
    print('o novo salário do funcionário é R$ {:.2f}'.format(S * 1.15))
else:
    print('o novo salário do funcionário é R$ {:.2f}'.format(S * 1.10))

#desafio 35: ler o comprimento de três retas e mostrar se elas podem ou não formar um triângulo
r1 = float(input('digite o comprimento da primeira reta: '))
r2 = float(input('digite o comprimento da segunda reta; '))
r3 = float(input('digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('as retas podem formar um triângulo')
else:
    print('as retas não podem formar um triângulo')