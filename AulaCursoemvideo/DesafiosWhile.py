#desafio 57 - Ler o sexo de uma pessoa, mas só aceitar M ou F. Caso esteja errado, pedir a digitação novamente até ter um valor correto.
c = ''
while c != 'M' and c != 'F':
    c = str(input('Digite o sexo [M/F]: ')).upper()
print(f'Sexo {c} registrado com sucesso!')

#desafio 58: jogo de adivinhação. O computador vai pensar em um número entre 0 e 10, e o jogador tem que tentar adivinhar qual é. O programa deve escrever na tela se o jogador venceu ou perdeu, e quantas tentativas foram necessárias para vencer.
from random import randint
n = randint(0, 10)
print('Sou seu computador, acabei de pensar em um número entre 0 e 10. Será que você consegue adivinhar qual é?')
c = -1 #o valor de c tem que ser diferente do valor de n para entrar no while, por isso coloquei -1, já que n é um número entre 0 e 10.
tentativas = 0
while c != n:
    c = int(input('Digite um número: '))
    tentativas += 1
    if c < n:
        print('Mais... Tente novamente.')
    elif c > n:
        print('Menos... Tente novamente.')
print(f'Parabéns! Você acertou o número {n} em {tentativas} tentativas!')

#desafio 59: Ler dois valores e mostrar um menu na tela: [1] somar, [2] multiplicar, [3] maior, [4] novos números, [5] sair do programa. O programa deve realizar a operação escolhida pelo usuário.
somar = 1
multiplicar = 2
maior = 3
novos_numeros = 4
sair = 5
a = 0
while a != sair:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print('''Escolha a operação:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    a = int(input('Digite a opção desejada: '))
    if a == somar:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
    elif a == multiplicar:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}.')
    elif a == maior:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}.')
        elif n2 > n1:
            print(f'O maior número entre {n1} e {n2} é {n2}. ')
        else:
            print(f'Os números {n1} e {n2} são iguais. ')
    elif a == novos_numeros:
        print('Digite os novos números: ')
    elif a == sair:
        print('Saindo do programa... ')

#desafio 60: Ler um número e mostrar o fatorial desse número.
n = int(input('Digite um Numero para ver seu fatorial: '))
F = 1
c = n
while c > 1:
    F *= c
    c -= 1
print(f'o valor de {n} fatorial é {F}')

#desafio 61: PA - Ler o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão.
p1 = int(input('digite o primeiro termo da PA: '))
r = int(input('digite a razao da PA: '))
c = 1
termo = p1
while c <= 10:
    print(f'{termo}', end=' -> ')
    termo += r
    c += 1
print('fim')

#desafio 62
p1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razao: '))
limite = int(input('digite ate quando voce deseja ver a pa; '))
termo = p1
c = 1
while c <= limite:
    print(f'{termo}', end=' -> ')
    termo += r
    c += 1
print('fim')

#desafio 63: fibonacci 
n = int(input('quantos termos voce quer ver: '))
t1 = 0
t2 = 1
c = 3 #ja vou mostar os 3 primeiros
print(f'{t1} -> {t2}', end= ' -> ')
while c <= n:
    t3 = t1 + t2
    print(f'{t3}', end= ' -> ')
    #atualzando os valores para o proximo ciclo
    t1 = t2
    t2 = t3 
    c += 1
print('fim')

#desafio 64:
n = 0
c = 0
x = 0
while n != 999:
    n = int(input('digite um valor (se esse valor for igual a 999 o programa para): '))
    x += n
    c += 1
print(f'foram digitados {c} numeros e o somatorio é {x}')

#desafio 65:
c = 'S'
l = []
while c == 'S':
    n = int(input('digite um valor: '))
    l.append(n)
    media = sum(l) / len(l)
    maior = max(l)
    menor = min(l)
    c = str(input('voce deseja continuar? [S/N]: ').upper())
print(f'a media é {media:.2f}, o maior é {maior} e o menor é {menor}')

