#desafio 21: tocando música com o python
import pygame
input('aperte enter para tocar a música')
print('tocando a música latina 2 de franzoi e tunes')
pygame.init()
pygame.mixer.music.load('/Users/arthurfranzoifernandes/Library/Mobile Documents/com~apple~CloudDocs/latina 2.mp3')
pygame.mixer.music.play()
input('aperte enter para parar a música')
pygame.mixer.music.stop()