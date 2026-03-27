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

pesado = max(pessoas)
magro = min(pessoas)

print('=-'*20)
print(f'foram cadastradas {cont} pessoas')
for p in pessoas:
    if p == pesado:
        print(f'o {p[0]} é o mais pesado com {p[1]}Kg')
    elif p == magro:
        print(f'o {p[0]} é o mais magro com {p[1]} Kg')