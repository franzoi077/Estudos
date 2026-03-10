#desafio 71:
print('-'*20)
print('BANCO FRANZOI')
print('-'*20)

valor = int(input('qual valor voce quer sacar ? '))             
notas = [50, 20, 10, 1]

for l in notas: #o 'l' pega um item da lista e executa ate acabar todos o itens da mesma lista
    quantidade = valor // l 
    valor %= l #atribui para o valor o resto de divisao do valor por l
    print(f'{quantidade} de notas de R${l},00')

