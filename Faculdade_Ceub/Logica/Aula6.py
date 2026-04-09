#1045
a, b, c = map(float, input('digite os tres lados do triangulo: ').split())
if a < b + c and b < a + c and c < a + b:
    #verificando se é acutangulo, retangulo ou obtusangulo
    if a*2 < b*2 + c*2 and b*2 < a*2 + c*2 and c*2 < a*2 + b*2:
        print('triangulo acutangulo')
    elif a*2 == b*2 + c*2 or b*2 == a*2 + c*2 or c*2 == a*2 + b*2:
        print('triangulo retangulo')
    else:
        print('triangulo obtusangulo')
    #verificando se é equilatero, isosceles ou escaleno
    if a == b == c:
        print('triangulo equilatero')
    elif a == b or b == c or a == c:
        print('triangulo isosceles')
    else:
        print('triangulo escaleno')
else:
    print('não forma triangulo')

#1046
from datetime import datetime
hora_inicial, hora_final = map(int, input('digite a hora inicial e a hora final do jogo: ').split())
if hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
else:
    duracao = (24 - hora_inicial) + hora_final
print(f'o jogo durou {duracao} hora(s)')

#1047
hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input('digite a hora inicial, minuto inicial, hora final e minuto final do jogo: ').split())
duracao_hora = 0
duracao_minuto = 0

if hora_inicial < hora_final:
    duracao_hora = hora_final - hora_inicial
else:
    duracao_hora = (24 - hora_inicial) + hora_final #calculando a duracao em horas, caso a hora final seja menor que a hora inicial, ou seja, o jogo tenha durado mais de 24 horas

if minuto_inicial < minuto_final:
    duracao_minuto = minuto_final - minuto_inicial
else:
    duracao_minuto = (60 - minuto_inicial) + minuto_final #calculando a duracao em minutos, caso o minuto final seja menor que o minuto inicial, ou seja, o jogo tenha durado mais de 60 minutos
    duracao_hora -= 1
print(f'o jogo durou {duracao_hora} hora(s) e {duracao_minuto} minuto(s)')

#1048
salario = float(input('digite o salario do funcionario: '))
if salario <= 400:
    aumento = salario * 0.15
    percentual = 15
elif salario <= 800:
    aumento = salario * 0.12
    percentual = 12
elif salario <= 1200:
    aumento = salario *0.10
    percentual = 10
elif salario <= 2000:
    aumento = salario * 0.07
    percentual = 7
else:
    aumento = salario * 0.04
    percentual = 4

novo_salario = salario + aumento
print(f'novo salario: {novo_salario:.2f}')
print(f'aumento: {aumento:.2f}')
print(f'percentual: {percentual} %')

#1050:
codigo = int(input('digite o codigo da cidade: '))
if codigo == 61:
    print('Brasilia')
elif codigo == 71:
    print('Salvador')
elif codigo == 11:
    print('Sao Paulo')
elif codigo == 21:
    print('Rio de Janeiro')
elif codigo == 32:
    print('Juiz de Fora')
elif codigo == 19:
    print('Campinas')
elif codigo == 27:
    print('Vitoria')
elif codigo == 31:
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')

#1051:
salario = float(input('digite o salario do funcionario: '))
if salario <= 2000:
    print('Isento')
elif salario <= 3000:
    imposto = (salario - 2000) *0.08
    print(f'R$ {imposto:.2f}')
elif salario <= 4500:
    imposto = (salario - 3000) * 0.18 + 1000 * 0.08 #calculando o imposto, caso o salario seja maior que 3000, ou seja, o funcionario pague imposto sobre os primeiros 1000 reais e sobre o valor que ultrapassar os 3000 reais
    print(f'R$ {imposto:.2f}')
else:
    imposto = (salario - 4500) * 0.28 + 1500 * 0.18 + 1000 * 0.08 #calculando o imposto, caso o salario seja maior que 4500, ou seja, o funcionario pague imposto sobre os primeiros 1000 reais, sobre os próximos 1500 reais e sobre o valor que ultrapassar os 4500 reais
    print(f'R$ {imposto:.2f}')

#1052 v1:
import calendar
import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

mes = int(input('digite o numero do mes: '))
print(calendar.month_name[mes])

#1052 v2:
mes = int(input('digite o numero do mes: '))
if mes == 1:
    print('janeiro')
elif mes == 2:
    print('fevereiro')
elif mes == 3:
    print('março')
elif mes == 4:
    print('abril')
elif mes == 5:
    print('maio')
elif mes == 6:
    print('junho')
elif mes == 7:
    print('julho')
elif mes == 8:
    print('agosto')
elif mes == 9:
    print('setembro')
elif mes == 10:
    print('outubro')
elif mes == 11:
    print('novembro')
elif mes == 12:
    print('dezembro')
else:
    print('mes invalido')

#1059:
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
