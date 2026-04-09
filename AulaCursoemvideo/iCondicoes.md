#if é uma estrutura de decisão, ou seja, ela é usada para tomar decisões com base em condições. A sintaxe básica do if é a seguinte:
# if condição:
#     bloco de código
# O bloco de código é executado apenas se a condição for verdadeira. Se a condição for falsa, o bloco de código é ignorado e o programa continua a execução normalmente.
#else é uma estrutura de decisão que é usada para executar um bloco de código quando a condição do if é falsa. A sintaxe básica do else é a seguinte:
# if condição:
#     bloco de código 1
# else:
#     bloco de código 2
# O bloco de código 1 é executado apenas se a condição for verdadeira, enquanto o bloco de código 2 é executado apenas se a condição for falsa. O else é opcional, ou seja, você pode usar apenas o if sem o else, mas não pode usar o else sem o if.
#ex:
idade = int(input('qual é a idade do seu carro?: '))
if idade <= 3:
    print('carro novo, parabéns!')
else:
    print('carro velho, cuidado!')
print('fim do programa')

#podemos tambem simplificar o código usando o operador ternário, que é uma forma mais concisa de escrever um if-else. A sintaxe básica do operador ternário é a seguinte:
#ex:
idade = int(input('qual é a idade do seu carro?: '))
print('carro novo, parabéns!' if idade <= 3 else 'carro velho, cuidado!')
print('fim do programa')

#exemplos:
#1
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'a sua média foi {m:.1f}')
if m >= 6.0:
    print('você está na média, parabéns!')
else:
    print('você está abaixo da média, estude mais!')