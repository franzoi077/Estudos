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