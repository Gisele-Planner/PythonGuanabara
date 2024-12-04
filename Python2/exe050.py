#Exercício Python #050 - Soma dos pares -> https://www.youtube.com/watch?v=rJaBLOW57Jg
from time import sleep

print(('==*==')*20)
print('Bem vindo(a) a Soma dos pares')
print(('==*==')*20)

n1 = int(input("Digite um número Inteiro: "))
n2 = int(input("Digite um número Inteiro: "))
n3 = int(input("Digite um número Inteiro: "))
n4 = int(input("Digite um número Inteiro: "))
n5 = int(input("Digite um número Inteiro: "))
n6 = int(input("Digite um número Inteiro: "))
lista = (n1,n2,n3,n4,n5,n6)

print(('\nProcessando...\n'))
sleep(1)

soma = 0
contagem = 0
for c in lista:
    if c % 2 == 0:
        contagem += 1
        soma += c
    
print(f'A soma dos {contagem} números pares digitados é: {soma}')
