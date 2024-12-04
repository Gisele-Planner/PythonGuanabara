# Exercicio 033 - Maior ou menor -> https://www.youtube.com/watch?v=a_8FbW5oH6I&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=34&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Maior ou Menor')
print(('==*==')*20)

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
lista = [n1,n2,n3]
print(f'O Maior número entre ({n1}, {n2} e {n3}) é: {max(lista)} e o Menor: {min(lista)} ')
