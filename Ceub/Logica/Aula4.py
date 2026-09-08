#1036:
import math
a, b, c = map(float, input('digite os 3 valores para a analise: ').split())
delta = b**2 - 4*a*c
if delta < 0 or a == 0:
    print('impossivel calcular')
else:
    r1 = (-b + math.sqrt(delta)) / (2*a)
    r2 = (-b - math.sqrt(delta)) / (2*a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')  