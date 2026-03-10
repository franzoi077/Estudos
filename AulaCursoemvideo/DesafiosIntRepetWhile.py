#desafio 66:
n = s = 0
while True:
    n = int(input('Digite um Número: '))
    if n == 999:
        break
    s += n
print(f'a soma é {s}')

#desafio 67: V1
a = b = 0
l = []
while True:
    a = int(input('digite um numero para ver sua tabuada: '))
    for d in range(1, 11):
        b = a * d
        l.append(b)
    if a < 0:
        break
    print(f'a tabuada de {a} é {l}')

#desafio 67: V2
a = 0
while True:
    a = int(input('digite um numero para ver sua tabuada: '))
    for i in range(1, 11):
        print(f'{a} X {i} = {a*i}')
    if a < 0:
        break

#desafio 68:
from random import randint
a = 0
b = randint(1, 10)
vitorias = 0
while True:
    c = str(input('voce quer par ou impar ? ').upper())
    a = int(input('vamos jogar par o impar, digite um valor: '))
    print(f'o computador escolheu: {b}')
    if (a + b) % 2 == 0 and c == 'PAR':
        print('voce ganhou, continue !')
        vitorias += 1
    elif (a + b) % 2 != 0 and c == 'IMPAR':
        print('voce ganhou, continue !')
        vitorias += 1
    else:
        print('voce perdeu')
        break
print(f'o seu numero de vitorias foi: {vitorias}')

#desafio 69:
mulher_com_20_anos = 0
homem = 0
idade = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    x = int(input('digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('voce é homem ou mulher ? [M/F]').strip().upper()[0])
    if x > 18:
        idade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and x < 20:
        mulher_com_20_anos += 1
    a = str(input('voce quer cadastrar mais alguel: ?[S/N]').upper())
    if a == 'N':
        break
print(f'{idade} tem 18 anos')
print(f'{homem} homens foram cadastrados')
print(f'{mulher_com_20_anos} mulheres com menos de 20 anos')
#para contagens o uso de if em sequencia é mais adequado que o uso de varios elif's

#desafio 70:
total_gasto = mais_de_mil = cont = menor_preco =  0
barato = ''
while True:
    print('-'*20)
    print('REGISTRO DE PRODUTOS')
    print('-'*20)
    
    nome = str(input('digite o nome do produto ? '))
    preco = int(input('digite o preço do seu produto ? '))
    cont += 1  #registra quantos produtos foram colocados no  registro  

    if cont == 1 or preco < menor_preco: #considera o primeiro produto o mais barato ate o momento em que o programa encontar um produto mais barato por meio do preco < menor_preco
        menor_preco = preco
        barato = nome

    total_gasto += preco #somando todos os proços   
    if preco > 1000:
        mais_de_mil += 1 

    x = ''
    while x not in 'SN':
        x = str(input('voce quer continuar ?  [S/N]').strip().upper()[0])
    if x == 'N':
        break

print(f'{"FIM DO PROGRAMA ":=ˆ40}')
print(f'o total gasto na contro foi de {total_gasto:.2f}')
print(f'{mais_de_mil:.2f} custam mais de mil reais')
print(f'{barato} é o produto mais barato e custa {menor_preco:.2f}')

#desafio 71:
print('-'*20)
print('BANCO FRANZOI')
print('-'*20)
valor = int(input('qual valor voce quer sacar ? '))             
notas = [50, 20, 10, 1]
for l in notas: #o 'l' pega um item da lista e executa ate acabar todos o itens da mesma lista
    quantidade = valor // l 
    valor %= l #atribui para o valor o resto de divisao do valor por l
    print(f'{quantidade} de notas de R${l},00')
