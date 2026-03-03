#desafio 36: emprestimo bancário
salario = float(input('qual é o salário do comprador? '))
valor_casa = float(input('qual é o valor da casa? '))
anos = int(input('em quantos anos o comprador pretende pagar? '))
prestacao_mensal = valor_casa / (anos * 12)
if prestacao_mensal > salario * 0.30:
    print('o empréstimo foi negado!')
else:
    print('o empréstimo foi aprovado!')

#desafio 37: conversor de bases numéricas
num = int(input('digite um número inteiro: '))
print('escolha a base de conversão: ')
print('1 - binário')
print('2 - octal')
print('3 - hexadecimal')
opcao = int(input('sua opção: '))
if opcao == 1:
    print(f'o número {num} em binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'o número {num} em octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'o número {num} em hexadecimal é {hex(num)[2:]}')
else:
    print('opção inválida!')

#desafio 38: comparar dois números
n1 = float(input('digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))
if n1 > n2:
    print(f'o número {n1} é maior que o número {n2}')
elif n2 > n1:
    print(f'o número {n2} é maior que o número {n1}')
else:
    print('os números são iguais!')

#desafio 39: ler a idade de um jovem e mostrar se ele ainda vai se alistar, se é a hora de se alistar ou se já passou do tempo de alistamento. O programa também deve mostrar o tempo que falta ou que passou do prazo
from datetime import date
ano_atual = date.today().year
ano_de_nascimento = int(input('digite o ano de nascimento do jovem: '))
idade = ano_atual - ano_de_nascimento
if idade < 18:
    print(f'você ainda vai se alistar, faltam {18 - idade} anos para o alistamento')
elif idade == 18:
    print('é hora de se alistar!')
else:
    print(f'você já passou do tempo de alistamento, passou {idade - 18} anos do prazo')

#desafio 40: ler três notas de um aluno e mostrar a média. A partir da média, mostrar a mensagem "APROVADO" se a média for maior ou igual a 7, "REPROVADO" se a média for menor que 5 e "RECUPERAÇÃO" se a média for entre 5 e 6.9
n1 = float(input('digite a primeira nota do aluno: '))
n2 = float(input('digite a segunda nota do aluno: '))
n3 = float(input('digite a terceira nota do aluno: '))
media = (n1 + n2 + n3) / 3
if media >= 7:
    print('APROVADO')
elif media < 5:
    print('REPROVADO')
else:
    print('RECUPERAÇÃO')

#desafio 41: ler o ano de nascimento de uma pessoa e mostrar sua categoria de acordo com a idade: "MIRIM" para até 9 anos, "INFANTIL" para até 14 anos, "JUNIOR" para até 19 anos, "SÊNIOR" para até 25 anos e "MASTER" para acima de 25 anos
ano_atual = date.today().year
ano_de_nascimento = int(input('digite o ano de nascimento da pessoa: '))
idade = ano_atual - ano_de_nascimento
if idade <= 9:
    print('a categoria da pessoa é MIRIM')
elif idade <= 14:
    print('a categoria da pessoa é INFANTIL')
elif idade <= 19:
    print('a categoria da pessoa é JUNIOR')
elif idade <= 25:
    print('a categoria da pessoa é SÊNIOR')
else:
    print('a categoria da pessoa é MASTER')

#desafio 42: ler o comprimento de três retas e mostrar se elas podem ou não formar um triângulo. Se elas puderem formar um triângulo, mostrar se ele é equilátero, isósceles ou escaleno
r1 = float(input('digite o comprimento da primeira reta: '))
r2 = float(input('digite o comprimento da segunda reta: '))
r3 = float(input('digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('as retas podem formar um triângulo')
    if r1 == r2 == r3:
        print('o triângulo é equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('o triângulo é isósceles')
    else:
        print('o triângulo é escaleno')
else:
    print('as retas não podem formar um triângulo')

#desafio 43: ler o peso e a altura de uma pessoa e mostrar seu índice de massa corporal (IMC) e sua classificação de acordo com a tabela abaixo:
peso = float(input('qual é o seu peso em kg? '))
altura = float(input('qual é a sua altura em metros? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'seu IMC é {imc:.2f}, você está abaixo do peso')
elif imc < 25:
    print(f'seu IMC é {imc:.2f}, você está com o peso ideal')
elif imc < 30:
    print(f'seu IMC é {imc:.2f}, você está com sobrepeso')
elif imc < 40:
    print(f'seu IMC é {imc:.2f}, você está com obesidade')
else:
    print(f'seu IMC é {imc:.2f}, você está com obesidade mórbida')

#desafio 44: calcular o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento. Utilize os códigos a seguir para ler qual é a condição de pagamento escolhida e efetuar o cálculo adequado:
preco = float(input('qual é o preço do produto? '))
print('condição de pagamento: ')
print('1 - à vista dinheiro/cheque: 10% de desconto')
print('2 - à vista cartão: 5% de desconto')
print('3 - em até 2x no cartão: preço normal')
print('4 - em 3x ou mais no cartão: 20% de juros')
condicao = int(input('qual é a condição de pagamento? '))
if condicao == 1:
    print(f'o valor a ser pago é R$ {preco * 0.90:.2f}')
elif condicao == 2:
    print(f'o valor a ser pago é R$ {preco * 0.95:.2f}')
elif condicao == 3:
    print(f'o valor a ser pago é R$ {preco:.2f}')
elif condicao == 4:
    print(f'o valor a ser pago é R$ {preco * 1.20:.2f}')
else:
    print('condição de pagamento inválida!')

#desafio 45: jogo de pedra, papel e tesoura
from random import choice
opcoes = ['pedra', 'papel', 'tesoura']
computador = choice(opcoes)
jogador = input('escolha pedra, papel ou tesoura: ').lower()
print(f'o computador escolheu {computador}')
if jogador == computador:
    print('empate!')
elif (jogador == 'pedra' and computador == 'tesoura') or (jogador == 'papel' and computador == 'pedra') or (jogador == 'tesoura' and computador == 'papel'):
    print('você ganhou!')
else:
    print('você perdeu!')

