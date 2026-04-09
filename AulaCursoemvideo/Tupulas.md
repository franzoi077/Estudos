#Tuplas

#exemplos de tuplas
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[0]) #imprime o primeiro elemento
print(lanche[1]) #imprime o segundo elemento
print(lanche[2]) #imprime o terceiro elemento
print(lanche[3]) #imprime o quarto elemento
#tentando alterar um elemento da tupla (isso vai gerar um erro)
#lanche[0] = 'hot dog' #isso vai gerar um erro, pois as tuplas são imutaveis


#podemos criar uma nova tupla a partir de uma tupla existente
nova_lanche = lanche + ('refrigerante', 'sorvete')
print(nova_lanche) #imprime a nova tupla


#podemos também criar uma tupla a partir de uma lista
minha_lista2 = ['hamburguer', 'suco', 'pizza', 'pudim']
minha_tupla3 = tuple(minha_lista2)
print(minha_tupla3) #imprime a tupla criada a partir da lista


#usando tupula com for
for comida in lanche:
    print(f'Eu vou comer {comida}') #imprime cada elemento da tupla
print('Comi pra caramba!') #imprime uma mensagem após o loop


#usando a função len() para saber quantos elementos tem na tupla
print(len(lanche)) #imprime o número de elementos da tupla


#usando a função sorted() para ordenar os elementos da tupla
print(sorted(lanche)) #imprime a tupla ordenada


#usando a função count() para contar quantas vezes um elemento aparece na tupla
print(lanche.count('pizza')) #imprime o número de vezes que 'pizza' aparece na tupla


#usando a função index() para saber a posição de um elemento na tupla
print(lanche.index('suco')) #imprime a posição de 'suco'   


#exemplo do curso em video
lanche = ('hamburguer', 'suco', 'pizza', 'pudim',  'batata frita')
for cont in range(0, len(lanche)): #o range ignora o ultimo valor da tupla, ou seja, o 5
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}') #imprime cada elemento da tupla
print('Comi pra caramba!') #imprime uma mensagem após o loop 

for pos, lanche in enumerate(lanche): #o enumerate retorna a posição e o valor do elemento da tupla
    print(f'Eu vou comer {lanche}, na posição {pos}') #imprime cada elemento da tupla
print('Comi pra caramba!') #imprime uma mensagem após o loop

a = (2, 5 , 4)
b = (5, 8, 1, 2)
c = a + b #é diferente de b + a, pois a ordem dos elementos é diferente
print(c) #imprime a tupla c, que é a junção das tuplas a e b
print(len(c)) #imprime o número de elementos da tupla c
print(c.count(5)) #imprime o número de vezes que o elemento 5 aparece na tupla c
print(c.index(8)) #imprime a posição do elemento 8 na tupla c
print(c.index(5)) #imprime a posição do primeiro elemento 5 na tupla c
print(c.index(5, 1)) #imprime a posição do elemento 5 na tupla c, a partir da posição 1

pessoa = ('Arthur', 25, 'M', 70.5)
del pessoa #deleta a tupla pessoa
#print(pessoa) #isso vai gerar um erro, pois a tupla foi deletada