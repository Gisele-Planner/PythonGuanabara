#Exercicio 19 - Sorteio de alunos -> https://www.youtube.com/watch?v=_Nk02-mfB5I&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=20&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Sorteio de Alunos')
print(('==*==')*20)

from random import choice
aluno1 = input("Digite nome do Aluno 1: ")
aluno2 = input("Digite nome do Aluno 2: ")
aluno3 = input("Digite nome do Aluno 3: ")
aluno4 = input("Digite nome do Aluno 4: ")
lista = [aluno4,aluno1,aluno2,aluno3]

print(f"O aluno sorteado foi: {choice(lista)}")