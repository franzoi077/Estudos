#1012:
a, b, c = map(float, input('digite os valores que deseja: ').split())
pi = 3.14159
print(f'TRIANGULO: {(a * c) / 2:.3f}')
print(f'CICULO: {pi * c ** 2:.3f}')
if a > b:
    print(f'TRAPEZIO: {(a + b) * c / 2:.3f}')
else:
    print(f'TRAPEZIO: {(b + a) * c / 2:.3f}')
print(f'QUADRADO: {b ** 2:.3f}')
print(f'RETANGULO: {a * b:.3f}')

#1013
a, b, c = map(float, input('digite tres valores: ').split())
if a > b and a > c:
    print(f'{a} eh maior')
elif b > a and b > c:
    print(f'{b} eh maior')
else:
    print(f'{c} eh maior:')

#1014
X = int(input('Quantos km voce percorreu? '))
Y = float(input('Quanto de combustivel voce gastou? '))
print(f'{X / Y} km/l')

#1015
from math import ceil, sqrt
x1, y1 = map(float, input('digite o p1: ').split())
x2, y2 = map(float, input('digite o p2: ').split())
d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'{ceil(d):.4f}')

#1016
d = int(input('digite a distancia que o carro X vai ter de Y: '))
print(f'{d * 2} minutos')
