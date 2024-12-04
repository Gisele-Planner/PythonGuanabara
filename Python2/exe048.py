#Exercício Python #048 - Soma ímpares múltiplos de três -> https://www.youtube.com/watch?v=iHjsUxNA-wo
from time import sleep

print(('==*==')*20)
print('Bem vindo(a) a Soma ímpares múltiplos de três')
print(('==*==')*20)

print(('\nProcessando...\n'))
sleep(1)
soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += c
    
print(f'A soma dos impáres múltiplos de 3 é igual a: {soma}')
