#conceito:
#as listas guaram valores como as tupulas so que as listas são MUTAVEIS

#Metados:
#o .append adiciona um valor a lista
#o .insert adiciona um valor a lista em uma posição especifica
#o .pop remove um valor da lista, se não for especificado o valor ele remove o ultimo valor da lista
#o .remove remove um valor da lista, se houver mais de um valor igual ele remove o primeiro valor encontrado
#o .sort ordena a lista em ordem crescente, se for especificado o parametro reverse=True ele ordena a lista em ordem decrescente
#o .len retorna o tamanho da lista
#o .count retorna a quantidade de vezes que um valor aparece na lista
#o .index retorna a posição de um valor na lista, se houver mais de um valor igual ele retorna a posição do primeiro valor encontrado
#o .clear limpa a lista, ou seja, remove todos os valores da lista
#o .copy retorna uma cópia da lista
#o .extend adiciona os valores de uma lista a outra lista
#o .reverse inverte a ordem dos valores da lista
#o .sum retorna a soma dos valores da lista, se a lista for composta por valores numéricos
#o .max retorna o maior valor da lista, se a lista for composta por valores numéricos
#o .min retorna o menor valor da lista, se a lista for composta por valores numéricos

#ex:
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0) #coloca no posição 2 o valor 0
if 5 in num:
    num.remove(5)
else:
    print('o numero 5 não foi encontrado')
num.pop(2) 
print(num)
print(f'Essa Lista tem {len(num)} elementos.')

#separando um ex do outro
print('-'*20)
print('separando um ex do outro')
print('-'*20)

#ex:
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('cheguei ao fim')

#separando um ex do outro
print('-'*20)
print('separando um ex do outro')
print('-'*20)

#ex
valores = []
for cont in range(0, 2):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('cheguei ao fim')

#separando um ex do outro
print('-'*20)
print('separando um ex do outro')
print('-'*20)

#ex:
a = [2, 3, 4, 7]
#isso é uma ligação: b = a #quando voce iguala duas listas o python cria uma ligação entre eleas !
b = a[:] #isso é uma copia da lista 'a'
b[2] = 8
print(f'lsita A: {a}')
print(f'lista B: {b}')