#Exercício Python #052 - Números primos -> https://www.youtube.com/watch?v=Er5Hyd4LyVw&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=20
from time import sleep

print(('\033[30m==*==')*20)
print('Bem vindo(a) aos Números Primos')
print(('==*==')*20)

número = int(input('Digite um número inteiro: '))
contador = 0

for c in range(1,número+1):
    if número % c == 0:
        print(f'\033[33m{c}', end = ' ')
        contador += 1 
    else:
        print(f'\033[31m{c}', end = ' ')

if contador == 2:
    print(f'\n\033[30mO número {número} foi divisivel {contador} vezes.')  
    print(f'E por isso, ele \033[33mé PRIMO!.')  
else:
    print(f'\n\033[30mO número {número} foi divisivel {contador} vezes.')  
    print(f'E por isso, ele \033[31mnão é PRIMO!.')  

