#Exercício Python #091 - Jogo de Dados em Python

print(('====')*20)
print('Bem vindo(a) - Jogo de Dados em Python')
print(('====')*20)

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6),
}
ranking = {}
print('Valores Sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)

print(('====')*20)
print(f'{"== Ranking dos Jogadores ==":^40}')
for p,e in enumerate(ranking):
    print(f'{p+1}º Lugar: {e[0]} com {e[1]}')
    sleep(1)
print(('====')*20)
