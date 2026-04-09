#o Whiel true cria um loop infinito
#o Break interrompe a repetição do loop While
n = cont = 0
while cont < 3:
    n = int(input('digite um numero: '))
    cont += 1

#gambiarra, jeito errado:
n = s = 0
while n != 999:
    n = int(input('digite um numero: '))
    s += n
s -= 999
print(f'a soma é {s}')

#jeito certo:
n = s = 0
while True:
    n = int(input('digite um numero: '))
    if n == 999:
        break
    s += n
print(f'a soma é {s}')
