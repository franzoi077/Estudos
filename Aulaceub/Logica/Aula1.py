#quando o código da erro, geralmente esta na linha anterior a linha do erro
#primeiro códgo: 
print("Olá, mundo!")

#segundo código:
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
print(f'a soma é igual a {n1 + n2}')
#a função f ela executa todas as operações dentro das chaves, e depois converte o resultado para string, e depois concatena com o restante da string, executando todas os input`s antes de executar a função print.


#terceirto código:
pi = 3.14159
R = float(input('digite o valor do raio: '))
A = pi * R ** 2
print('A área do círculo é igual a {:.4f}'.format(A))
#o uso do {:.4f} é para limitar o número de casas decimais a 4, e o .format(A) é para substituir o {} pelo valor de A, e o resultado é convertido para string e concatenado com o restante da string.

#quarto código:
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média entre {} e {} é igual a {}'.format(n1, n2, m))

#quinto código:
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
n3 = float(input('digite a terceira nota: '))
M = (n1 * 2 + n2 * 3 + n3 * 5) / 10
print('A média ponderada entre {}, {} e {} é igual a {:.2f}'.format(n1, n2, n3, M))

#sexto código:
a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
c = int(input('digite o valor de c: '))
d = int(input('digite o valor de d: '))
delta = a * b - c * d
print('O valor de delta é igual a {}'.format(delta))