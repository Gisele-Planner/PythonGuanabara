#Exercício Python #088 - Palpites para a Mega Sena -> https://youtube.com/watch?v=Hd7Ycaj61xE&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=20

print(('==*==')*20)
print('Bem vindo(a) - Palpites para a Mega Sena')
print(('==*==')*20)
print('============MegaSena=================')

from random import randint
from time import sleep
número = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0,número):
    print()
    print(f'Jogo {i+1}: ',end = ' ')
    sleep(1)
    for n in range(6):        
        print(randint(1,60), end = ' ')
print(f'\n\n============Boa sorte!!==========')
