#Desafio 5: Antecessor e Sucessor
N = int(input('Digite um número: '))
print(f'o antecessor de {N} é {N - 1} e o sucessor de {N} é {N + 1}')
#o uso do f é para executar as operações dentro das chaves e depois converter o resultado para string e concatenar com o restante da string, e o uso do -1 e +1 é para calcular o antecessor e o sucessor do número digitado.

#Desafio 6: Dobro, Triplo e Raiz Quadrada
N = int(input('Digite um número: '))
print(f'o dobro de {N} é {N *2}, o triplo de {N} é {N * 3} e a raiz quadrada de {N} é {N ** (1/2):.2f}')
 
#Desafio 7: Média Aritmética
N1 = float(input('Digite a primeira nota: '))
N2 = float(input('Digite a segunda nota: '))
print(f'A média entre {N1} e {N2} é {(N1 + N2) / 2:.2f}')

#Desafio 8: Conversor de medidas
M = float(input('Digite a medida em metros: '))
print(f'{M} em centímetros é igual a {M * 100}cm e em milimetros é igual a {M * 1000}mm')
 
#Desafio 9: Tabuada de um número qualquer
N = int(input('Digite um número para ver a tabuada: '))
print(f'{N} x 1 = {N * 1}', end=', ')
print(f'{N} x 2 = {N * 2}', end=', ')
print(f'{N} x 3 = {N * 3}', end=', ')
print(f'{N} x 4 = {N * 4}', end=', ')
print(f'{N} x 5 = {N * 5}', end=', ')
print(f'{N} x 6 = {N * 6}', end=', ')
print(f'{N} x 7 = {N * 7}', end=', ')
print(f'{N} x 8 = {N * 8}', end=', ')
print(f'{N} x 9 = {N * 9}', end=', ')
print(f'{N} x 10 = {N * 10}')

#Deasafio 10: conversor de para Dolar
R = float(input('quanto voce tem na sua carteira? em reais: R$'))
print(f'com {R} reais voce pode comprar {R / 3.27 :.2f} dolares')

#Desafio 11: Area da parede e quantidade de tinta necessária para pintar a parede
L = float(input('Digite a largura da parede: '))
H = float(input('Digite a altura da parede: '))
print(f'A área da parede é igual a {L * H}m2', end=', ')
print(f'para pintar a parede voce precisa de {L * H / 2 :.2f} litros de tinta')

#Desafio 12: Desconto de 5% em um produto
P = float(input('Digite o preço do pruduto; R$'))
print(f'com o desconto de 5% o preço do produto é igual a R${P * 0.95:.2f}')

#Desafio 13: Aumento de 15% em um salário
S = float(input('Digite o salário do funcionário: R$'))
print(f'com o aumento de 15% o salário do funcionário é igual a R${S * 1.15:.2f}')