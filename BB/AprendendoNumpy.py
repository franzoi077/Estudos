import numpy as np 
#primeiros arreys
lista = [1, 2, 3, 4, 5]
array = np.array(lista)
print(array) #[1 2 3 4 5]

#arrays de zero e um
zeros = np.zeros((5, 5))   
print(zeros) #[0. 0. 0. 0. 0.]
uns = np.ones((2, 3))
print(uns) #[[1. 1. 1.]
              #[1. 1. 1.]]
            
#range do numpy
sequencia = np.arange(0, 10, 2) #começa em 0, vai até 10 e pula de 2 em 2
print(sequencia) #[0 2 4 6 8]

#loop no numpy
arr = np.array([1, 2, 3])
resultado = arr * 2
print(resultado) #[2 4 6]

#somando elemento por elemento
arr1 = np.array([1, 2, 3 ])
arr2 = np.array([4, 5, 6])
soma = arr1 + arr2
print(soma) #[5 7 9]

#indexação e cortes
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz[0, 1]) #2 (linha 0, coluna 1)
print(matriz[1:, 1:]) #[[5 6] (linha 1 e 2, coluna 1 e 2)
                      #[8 9]]

#primeiro desafio
a = np.arange(10, 50, 5) #começa em 10, vai até 50 e pula de 5 em 5 
sub = a - 2
sub[-1] = 100 #substitui o valor do índice 50 por 100
print(sub) #[  8  13  18  23  28  33  38 100]

