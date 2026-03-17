#desafio 72:
a = int(input('digite um numero de 0 a 20: '))
extenco = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
for c in extenco:
    if a == extenco.index(c):
        print(f'voce digitou o numero {c}')

#desfio 73:
tabela = ('corintias', 'palmeiras', 'santos', 'são paulo', 'flamengo', 'vasco', 'fluminense', 'botafogo', 'gremio', 'internacional', 'atletico-mg', 'atletico-pr', 'bahia', 'sport', 'vitória', 'chapecoense', 'avai', 'ceara', 'fortaleza', 'goias')
print('os 5 primeiros colocados são: ', tabela[:5])
print('os 4 ultimos colocados são: ', tabela[-4:])
print('os times em ordem alfabetica são: ', sorted(tabela))
print('o chapecoense esta na posição: ', tabela.index('chapecoense') + 1) #o index começa a contar do 0, por isso é necessário somar 1 para mostrar a posição correta do time na tabela

#deasfio 74:
import random
a = random.sample(range(1,100), 5)
print(sorted(a))
print(f'o maior valor é {max(a)}')
print(f'o menor valor é {min(a)}')

#desafio 75:
a = tuple(int(x)for x in input('Digite os numeros separdos por espaço: ').split())
print(a.count(9))
if 3 in a:
    print(a.index(3))
else:
    print('o numero 3 não foi encontrado')
for par in a:
    if par % 2 == 0:
        print(f'{par} é par')

#desafio 76:
x = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Conpasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*20)
print('Listagem de preços')
print('-'*20)
print(x[0], '.'*20, 'R$', x[1])
print(x[2], '.'*20, 'R$', x[3])
print(x[4], '.'*20, 'R$', x[5])
print(x[6], '.'*20, 'R$', x[7])
print(x[8], '.'*20, 'R$', x[9])
print(x[10], '.'*20, 'R$', x[11])
print(x[12], '.'*20, 'R$', x[13])
print(x[14], '.'*20, 'R$', x[15])
print(x[16], '.'*20, 'R$', x[17])

#desafio 77:
palavras = ('ola', 'hello', 'arthur', 'pedro',)
for d in palavras:
    a = d.count('a')
    e = d.count('e')
    i = d.count('i')
    o = d.count('o')
    u = d.count('u')
    print(f'a palavra {d} tem {a + e + i + o + u} vogais')