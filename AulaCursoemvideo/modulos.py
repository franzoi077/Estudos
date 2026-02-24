#import é uma palavra reservada do python para importar bibliotecas, módulos, etc
#from é uma palavra reservada do python para importar partes específicas de um módulo
#a forma de usar é form ... import algo especifico da biblioteca, módulo, etc
#math é uma biblioteca do python para realizar operações matemáticas e tem em suas funções diversas operações como trigonométricas, logaritmos, etc
#sqrt é uma função da biblioteca math para calcular a raiz quadrada
#floor é uma função da biblioteca math para arredondar para baixo
#ceil é uma função da biblioteca math para arredondar para cima
#trunc é uma função da biblioteca math para truncar um número, ou seja, remover
#pow é uma função da biblioteca math para calcular a potência de um número
#factorial é uma função da biblioteca math para calcular o fatorial de um número

from math import sqrt, ceil 
num = float(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, ceil(raiz)))

import random
num = random.randint(1, 25)
print('O número sorteado foi {}'.format(num))