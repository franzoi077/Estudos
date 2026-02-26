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
print(f'A área do círculo é igual a {A:.4f}')
#o uso do {:.4f} é para limitar o número de casas decimais a 4, e o .format(A) é para substituir o {} pelo valor de A, e o resultado é convertido para string e concatenado com o restante da string.

#quarto código:
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A média entre {n1} e {n2} é igual a {m:.2f}')

#quinto código:
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
n3 = float(input('digite a terceira nota: '))
M = (n1 * 2 + n2 * 3 + n3 * 5) / 10
print(f'A média ponderada entre {n1}, {n2} e {n3} é igual a {M:.2f}')

#sexto código:
a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
c = int(input('digite o valor de c: '))
d = int(input('digite o valor de d: '))
delta = a * b - c * d
print(f'O valor de delta é igual a {delta}')

#setimo código:
ni = float(input('digite seu numero de identificação: '))
hi = float(input('digite o número de horas trabalhadas: '))
vh = float(input('digite o valor que você recebe por hora: '))
print(f'o funcionário {ni} recebeu R$ {hi * vh:.2f} no mês')

#oitavo código:
nome = str(input('digite seu nome completo: ')).strip()
s = float(input('qual é o salário do funcionário? '))
v = float(input('qual é o valor das vendas do funcionário? '))
print(f'o salário total do funcionário {nome} é R$ {s + (v * 0.15):.2f}')

#nono código:
a = input('digite respectivamente o código, a quantidade e o valor unitário da peça 1: ').split()
cod1 = int(a[0])
qtd1 = int(a[1])
val1 = float(a[2])
b = input('digite respectivamente o código, a quantidade e o valor unitário da peça 2: ').split()
cod2 = int(b[0])
qtd2 = int(b[1])
val2 = float(b[2])
print(f'O valor a ser pago na peça 1 é R$ {qtd1 * val1:.2f}')
print(f'O valor a ser pago na peça 2 é R$ {qtd2 * val2:.2f}')
print(f'O valor total a ser pago é R$ {(qtd1 * val1) + (qtd2 * val2):.2f}')
#o uso do split() é para dividir a string em uma lista de palavras, usando o espaço como separador. O índice [0] é usado para acessar o primeiro elemento da lista, que é o código da peça, o índice [1] é usado para acessar o segundo elemento da lista, que é a quantidade de peças, e o índice [2] é usado para acessar o   terceiro elemento da lista, que é o valor unitário da peça. Portanto, a[0] retorna o código da peça, a[1] retorna a quantidade de peças e a[2] retorna o valor unitário da peça. O mesmo vale para a variável b.    

#decimo código:
pi = 3.14159
R = float(input('digite o valor do raio: '))
print(f'VOLUME  {(4.0 / 3.0) * pi * R ** 3:.3f}')
