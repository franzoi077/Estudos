#A ordem de execução dos operadores arítméticos é a seguinte:
#1. Parênteses ()
#2. Exponenciação **
#3. Multiplicação * e Divisão / e Resto %
#4. Adição + e Subtração - 
#ex:

n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
som = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
print('A soma é {},\n a subtração é {}, a multiplicação é {}'.format(som, sub, mult), end=', ')
print('A divisão é {:.2f} e a potência é {}'.format(div, pot))

#o uso do end=', ' é para evitar a quebra de linha e concatenar a próxima string com a anterior, e o uso do {:.2f} é para limitar o número de casas decimais a 2.
#o uso do \n é para quebrar a linha e imprimir a próxima string em uma nova linha.
