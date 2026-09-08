#1060:
positivo = negativo = 0
for c in range(6):
    a = float(input('digite um numero: '))
    if a > 0:
        positivo += 1
    elif a < 0:
        negativo += 1
print(f'{positivo} valores positivos')

#1061:
w = input('digite a data de inicio: ')
dias_inicio = int(w.split()[1])
x, y, z = map(int, input('digite a hora, minuto e segundo no formato hh:mm:ss: ').split(':'))

a = input('digite a data de termino: ')
dias_termino = int(a.split()[1])
b, c, d = map(int, input('digite a hora, minuto e segundo no formato hh:mm:ss: ').split(':'))

#caulculando a duracao do jogo em segundos, considerando os dias, horas, minutos e segundos
segundos_inicio = z + (y * 60) + (x * 3600) + (dias_inicio * 86400)
segundos_termino = d + (c * 60) + (b * 3600) + (dias_termino * 86400)
duracao = segundos_termino - segundos_inicio

if duracao < 0:
    print('a data de termino deve ser maior que a data de inicio')
    exit()

#calculando a duracao do jogo em dias, horas, minutos e segundos
dias = duracao // 86400
duracao %= 86400
horas = duracao // 3600
duracao %= 3600
minutos = duracao // 60
duracao %= 60

#imprimindo a duracao do jogo em dias, horas, minutos e segundos
print(f'{dias} dia(s)') 
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{duracao} segundo(s)')

#1064:
lista_positivos = []
positivo = 0

for c in range(6):
    a = float(input('digite um numero: '))
    if a > 0:
        positivo += 1
        lista_positivos.append(a)
media = sum(lista_positivos) / len(lista_positivos)

print(f'{positivo} valores positivos')
print(f'Media: {media:.1f}')

#1065:
par = 0
for c in range(5):
    a = int(input('digite um numero: '))
    if a % 2 == 0:
        par += 1
print(f'{par} valores pares')

#1066:
par = impar = positivo = negativo = 0
for c in range(5):
    a = int(input('digite um numero: '))
    if a % 2 == 0:
        par += 1
    else:
        impar += 1
    if a > 0:
        positivo += 1
    elif a < 0:
        negativo += 1
print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')

#1067:
impar = 0
a = int(input('digite um numero: '))
for c in range(1, a + 1, 2):
    print(c)