#desafio 16:
import math
num = float(input('digite um número real qualquer: '))
print('a parte inteira do número é {}'.format(math.trunc(num)))

#desafio 17 : catetos e hipotenusa
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
print('a hipotenusa é igual a {:.2f}'.format(math.hypot(co, ca)))