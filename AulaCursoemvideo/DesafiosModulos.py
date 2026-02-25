#desafio 16:
import math
num = float(input('digite um número real qualquer: '))
print('a parte inteira do número é {}'.format(math.trunc(num)))

#desafio 17 : catetos e hipotenusa
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
print('a hipotenusa é igual a {:.2f}'.format(math.hypot(co, ca)))

#desafio 18: seno, cosseno e tangente
angulo = float(input('digite o valor do ângulo: '))
print ('o seno do angulo é {:.2f}'.format(math.sin(angulo)))
print ('o cosseno do angulo é {:.2f}'.format(math.cos(angulo)))
print ('a tangente do angulo é {:.2f}'.format(math.tan(angulo)))

#desafio 19: sorteando um nome na aleatório
import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
print('o aluno escolhido foi {}'.format(random.choice([n1, n2, n3, n4])))

#desafio 20: sorteando a ordem de apresentação
import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: ')) 
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
print('a ordem de apresentação será: {}'.format(random.sample([n1, n2, n3, n4], k=4)))
#o random.sample() é usado para obter uma amostra aleatória de elementos de uma sequência, sem repetição. O parâmetro k especifica o número de elementos a serem selecionados. Neste caso, estamos selecionando os 4 alunos em uma ordem aleatória.

#desafio 21: tocando música com o python
import pygame
input('aperte enter para tocar a música')
print('tocando a música latina 2 de franzoi e tunes')
pygame.init()
pygame.mixer.music.load('/Users/arthurfranzoifernandes/Library/Mobile Documents/com~apple~CloudDocs/latina 2.mp3')
pygame.mixer.music.play()
input('aperte enter para parar a música')
pygame.mixer.music.stop()