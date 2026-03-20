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
