#desafio 78:
a = []
for c in range(0, 5):
    a.append(int(input('Digite um valor: ')))
print('=-'*20)
print(a)

maximo = max(a)
minimo = min(a)

#localizando o maior
print(f'o maior valor encontrado foi {maximo} e esta na posição', end='')
for i, v in enumerate(a):
    if v == maximo:
        print(f' {i}...', end='')
print()

#localizando o menor
print(f'o menor valor encontrado foi {minimo} e esta na posição', end= '')
for i, v in enumerate(a):
    if v == minimo:
        print(f' {i}...', end='')
print()


#desafio 79:
x = []
while True:
    a = (int(input('Digite um valor: ')))
    if a not in x:
        x.append(a)
        print('valor adicionado com sucesso')
    else:
        print('valor recusado, tente outro')
    #mecanismo de parada:
    j = ' '
    while j not in 'SN':
        j = str(input('voce quer continuar? [S/N]').strip().upper()[0])
    if j == 'N':
        break
print(f'os valores digitados foram {sorted(x, reverse=True)}')

#desafio 80:
lista = []
for c in range(0, 5):
    lista.append(int(input('digite um valor: ')))
n = len(lista) #realizar a ação em determinado tempo
for i in range(n): #bubble sort
    for j in range(0, n - i - 1): #manda o maior termo i para o final e quando roda novamente sabe que o ultimo termo é o maior e não compara com ele novamente, por ultilizar o - ele vai para o final. o -1 é para garantir que ele não vai tentar comparar um termo que não existe.
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j] #trocando eles de lugar
print(lista)

#deafio 81:
b = []
while True:
    a = int(input('digite um valor para ser adicionado na lista: '))
    b.append(a)
    #mecanismo de parada:
    c = ' '
    while c not in 'SN':
        c = str(input('voce quer continuar ? [S/N]').strip().upper()[0])
    if c == 'N':
        break
print('=-'*20)
print(f'a lista tem {len(b)} valores')
print('=-'*20)
print(f'a ordem decrescente da lista é {sorted(b, reverse=True)}')
print('=-'*20)
if 5 in b:
    print('o numero 5 esta na lista')
else:
    print('o valor 5 não esta na lista')
print('=-'*20)

#desafio 82:
numeros = []
par = []
impar = []

while True:
    a = int(input('digite um valor para ver se ele é par ou ímpar: '))
    numeros.append(a)
    
    #verificando se o nuemro é par :
    if a % 2 == 0:
        par.append(a)
    else:
        impar.append(a)
    
    #mecanismo de parada
    p = ' '
    while p not in 'SN':
        p = str(input('Voce quer continuar? [S/N]').strip().upper()[0])
    if p == 'N':
        break

numeros.sort()
par.sort()
impar.sort()

print(f'pares{par}')
print(f'impar{impar}')
print(f'todos os numeros{numeros}')

#desafio 83:
expressao = str(input('digite a expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo in '([{':
        pilha.append(simbolo)
    elif simbolo in ')]}':
        if len(pilha) == 0:
            pilha.append(')')
            break
        topo = pilha.pop()
        if topo == '(' and simbolo != ')':
            pilha.append(')')
            break
        if topo == '[' and simbolo != ']':
            pilha.append(')')
            break
        if topo == '{' and simbolo != '}':
            pilha.append(')')
            break
if len(pilha) == 0:
    print('a expressão é valida')
else:
    print('a expressão é invalida')

#deafio 84:
pessoas = []
individuo = []
cont = 0

while True:
    #cadastrando as pessoas
    individuo.append(str(input('Digite o nome; ')))
    individuo.append(int(input('Digite o peso: ')))
    pessoas.append(individuo[:])

    cont += 1
    
    individuo.clear() #limpando a lista para a proxima pessoa

    #mecanismo de parada:
    p = ' '
    while p not in 'SN':
        p = str(input('Voce quer continuar ? [S/N]').strip().upper()[0])
    if p == 'N':
        break

pesado = max(pessoas) #achando o mais pesado na lista
magro = min(pessoas) #achando o mais magro na lista

print('=-'*20)
print(f'foram cadastradas {cont} pessoas')
for p in pessoas:
    if p == pesado:
        print(f'o {p[0]} é o mais pesado com {p[1]}Kg') #p[0] retorna o primeiro elemento cadastrado e p[1] retorana o segudo elemento
    elif p == magro:
        print(f'o {p[0]} é o mais magro com {p[1]} Kg')

#desafio 85:
valores = [[], []]
for i in range(1, 8):
    valores.append(int(input(f'Digite o {i}° valor: ')))
    if valores[i] % 2 == 0:
        valores[0].append(valores[i])
    else:
        valores[1].append(valores[i])
print('=-'*20)
print(f'os valores pares digitados foram {sorted(valores[0])}')
print(f'os valores impares digitados foram {sorted(valores[1])}')

#deasfio 86:
matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3): #percorre as linhas e colunas da matriz, ou seja, percorre as posições da matriz
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
print('=-'*20)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='') #imprime a matriz formatada, ou seja, com os valores centralizados e com um espaço de 5 caracteres entre eles
    print() #quebra a linha para imprimir a proxima linha da matriz

#desafio 87:
matriz = [[], [], []]
soma = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
print('=-'*20)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print('=-'*20)
print(f'a soma dos valores pares é {soma}')
print(f'a soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'o maior valor da segunda linha é {max(matriz[1])}')

#desfio 88:
from random import randint
quantidade_jogos = int(input('quantos jogos voce quer que eu sorteie? '))
jogos = []
for i in range(0, quantidade_jogos):
    jogo = []
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogos.append(jogo)
print('=-'*20)
for i, jogo in enumerate(jogos):
    print(f'jogo {i+1}: {sorted(jogo)}')
        
#desafio 89:
alunos_notas = [[], [], []]
while True:
    alunos_notas[0].append(str(input('Digite o nome do aluno: ')))
    alunos_notas[1].append(float(input('Digite a  primeira nota do aluno: ')))
    alunos_notas[2].append(float(input('Digite a segunda nota do aluno: ')))
    #mecanismo de parada:
    p = ' '
    while p not in 'SN':
        p = str(input('Voce quer continuar? [S/N] ').strip().upper()[0])
    if p == 'N':
        break
print('=-'*20)
for i in range(0, len(alunos_notas[0])):
    media = (alunos_notas[1][i] + alunos_notas[2][i]) / 2
    print(f'{i} - {alunos_notas[0][i]} - {media:.1f}') #imprime o nome do aluno e a média das notas, ou seja, a soma das notas dividida por 2
