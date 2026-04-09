'''for c in range(1, 10):
    print(c)
print('fim')'''

'''a = 'S'
while a == 'S':
    c = int(input('Digite um valor: '))
    a = str(input('Quer continuar? [S/N] ')).upper()
print('fim')'''

c = 1
impar = par = 0
while c != 0:
    c = int(input('Digite um valor: '))
    if c % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares')