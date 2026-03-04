#desafio 46: contagem regressiva
for i in range(10, -1, -1):
    print(i, end=' ')
print('Feliz ano novo!')

#desafio 47: contagem de pares
for i in range(2, 51, 2):
    print(i, end=' ')
print('Acabou!')

#desafio 48: contagem de ímpares
for i in range(1, 500, 3):
    print(i, end=' ')
print('Acabou!')

#desafio 49: tabuada
n = int(input('Digite um número para ver sua tabuada: '))
for i in range(11):
    print(f'{n} x {i} = {n*i}', end=' ')
print('Acabou!')

#desafio 50: soma dos pares
s = 0 
for i in range(7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos números pares é {s}')

#desafio 51: progressão aritmética
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for i in range(10):
    print(a1 + i*r, end=' ')
print('Acabou!')

#desafio 52: números primos
n = int(input('Digite um número para saber se ele é primo: '))
tot = 0
for i in range(1, n + 1):
    if n % i == 0:
        tot += 1
if tot == 2:
    print(f'O número {n} é primo!')
else:
    print(f'O número {n} não é primo!')

#desafio 53: palíndromo
frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if junto == inverso:
    print(f'A frase é um palíndromo!')
else:
    print(f'A frase não é um palíndromo!')

#desafio 54: maior e menor idade
maior = 0 
meno = 0
for i in range (7):
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        maior += 1
    else:
        meno += 1
print(f'{maior} pessoas são maiores de idade e {meno} pessoas são menores de idade!')

#desafio 55: maior e menor peso
maior = 0
menor = 0
for i in range(5):
    peso = float(input('Digite o peso: '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}kg e o menor peso é {menor}kg!')

#desafio 56: análise de dados
soma = 0 
media = 0
maior = 0
tot = 0
for i in range (4):
    nome = str(input('digite o nome: ')).strip() #o strip() serve para remover os espaços em branco no início e no final da string, caso o usuário digite um nome com espaços, como " João ", o strip() vai remover os espaços e deixar apenas "João". O strip() é útil para evitar erros de digitação e garantir que o nome seja armazenado corretamente.
    idade = int(input('digite a idade: '))
    sexo = str(input('digite o sexo [M/F]: ')).strip().upper()
    soma += idade
    if i == 0 and sexo == 'M': #o i == 0 serve para garantir que o primeiro homem seja o mais velho, caso contrário, se o primeiro for mulher, o maior nunca será atualizado e o resultado final será 0, mesmo que haja homens no grupo.
        maior = idade
    if sexo == 'M' and idade > maior:
        maior = idade
    if sexo == 'F' and idade < 20:
        tot += 1
    media = soma / 4
print(f'A média de idade do grupo é {media:.2f} anos!')
print(f'O homem mais velho tem {maior} anos!')
print(f'Ao todo são {tot} mulheres com menos de 20 anos!')