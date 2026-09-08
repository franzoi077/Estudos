#1037
a = float(input('Digite um valor para ver seu intervalo: '))
if a > 0  and a <= 25:
    print('intervalo (0, 25]')
elif a > 25 and a <= 25:
    print('intervalor (25, 50]')
elif a > 50 and a <= 75:
    print('intervalo (50, 75]')
elif a > 75 and a <= 100:
    print('intervalo (75, 100]')
else:
    print('fora de intervalo')

 #1038:
produto = 0
while produto not in range(1, 6):
    produto, qunatidade = map(int, input('Digite o código do porduto e a quantidade: ').split())
if produto == 1:
    print(f'Total: R$ {qunatidade * 4:.2f}')
elif produto == 2:
    print(f'Total: R$ {qunatidade * 4.50:.2f}')
elif produto == 3:
    print(f'Total: R$ {qunatidade * 5:.2f}')
elif produto == 4:
    print(f'Total: R$ {qunatidade * 2:.2f}')
else:
    print(f'Total: R$ {qunatidade * 1.50:.2f}')

#1040:
n1, n2, n3, n4 = map(float, input('Digite as suas notas em ordem: ').split())
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4)) / 10
nova_media = 0
print(f'Media: {media:.1f}')
if media >= 7:
    print('Aluno aprovado')
elif media < 5:
    print('Aluno Repovado')
elif media >= 5 and media <= 6.9:
    print('Aluno em exame')
    exame = float(input('Nota do exame: '))
    nova_media = (exame + media) / 2
    if nova_media >= 5:
        print('Aluno aprovado')
    else:
        print('Aluno Repovado')
    print(f'Media final: {nova_media:.1f}')

#1041:
x, y = map(float, input('Digite x e y: '))
#origem:
if x == 0 and y == 0:
    print('origem')
#no eixo y
elif x == 0:
    print('no eixo Y')
#no eixo x
elif y == 0:
    print('no eixo X')
#no Q1
elif x > 0 and y > 0:
    print('Q1')
#no Q2
elif x < 0 and y > 0:
    print('Q2')
#no Q3
elif x < 0 and y < 0:
    print('Q3')
#no Q4
elif x > 0 and y < 0:
    print('Q4')

#1042:
numeros = list(map(int, input().split()))
DeNumeros = list(numeros)
numeros.sort()
for i in numeros:
    print(i)
print()
for n in DeNumeros:
    print(n)

#1043
r1 = float(input('digite o comprimento da primeira reta: ')) #a
r2 = float(input('digite o comprimento da segunda reta; ')) #b
r3 = float(input('digite o comprimento da terceira reta: ')) #c
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'perimeto = {r1 + r2 + r3}')
elif r1 > r2:
    print(f'area = {((r1 + r2) * r3) / 2}')
elif r2 > r1:
    print(f'area = {((r2 + r1) * r3) / 2}')

#1044
a, b = map(int, input('digite os valores para ver se são multiplos: ').split())
if a % b == 0 and b % a == 0:
    print('são multiplos')
else:
    print('não são multiplos')