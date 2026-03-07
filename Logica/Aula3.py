#1018: V2
valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
print(valor)
for a in notas:
    quantidade = valor // a
    valor %= a
    print(f'{quantidade} nota(s) de R$ {a},00')
 
# 1019: V1
s = int(input('digite os segundos: '))
horas = s // 3600
s %= 3600
minutos = s // 60
s %= 60
print(f'{horas}:{minutos}:{s}')

#1019: v2
s = int(input('digite os segundos para ter a converção: '))
resultados = []
divisores = [3600, 60]
for d in divisores:
    valor = s // d
    s %= d
    resultados.append(valor) #o append adiociona um item na lista ja existente
print(f'{resultados[0]}:{resultados[1]}:{s}')

#1020: v1
i = int(input('digite sua idade em dias: '))
anos = i // 360
i %= 360
meses = i // 30
i %= 30
print(f'{anos} anos(s)')
print(f'{meses} mes(es)')
print(f'{i} dia(s)')

#1020: v2
i = int(input('digite sua idade em dias: '))
resultados = []
divisores = [360, 30]
for d in divisores:
    valor = i // d
    i %= d
    resultados.append(valor)
print(f'''{resultados[0]}
{resultados[1]}
{i}''')

#1035:
a, b, c, d, =  map(int, input('digite os 4 valores para a analise: '))
if b > c and d > a and c + d > a + b and c >= 0 and d >= 0 and a % 2 == 0:
    print('valores aceitos')
else:
    print('valores nao aceitos')


