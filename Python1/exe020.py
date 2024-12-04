#Exercicio 20 - Sorteio de ordem de apresentação -> https://www.youtube.com/watch?v=OPh0nngbBSY&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=21&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Sorteio de Ordem de Apresentação')
print(('==*==')*20)

import random
aluno1 = input("Digite nome do Aluno 1: ")
aluno2 = input("Digite nome do Aluno 2: ")
aluno3 = input("Digite nome do Aluno 3: ")
aluno4 = input("Digite nome do Aluno 4: ")
lista = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(lista)
print(lista)