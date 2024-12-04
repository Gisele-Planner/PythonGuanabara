# Exercicio 21 - Ouvir Mp3 pelo Python - Funcionou no VSCode -> https://www.youtube.com/watch?v=9FiEji_fzvk&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=22&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Ouvir MP3')
print(('==*==')*20)

import pygame
pygame.init()
pygame.mixer.music.load('teste.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
