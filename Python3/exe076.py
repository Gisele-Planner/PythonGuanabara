#exercicio 076 - Lista de Preços com Tupla -> https://www.youtube.com/watch?v=Qp2cXfCHk2I&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=6

print(('==*==')*20)
print('Bem vindo(a) - Lista de Preços com Tupla')
print(('==*==')*20)

listagem = ('Lápis',1.25,
            'Caderno',21.5,
            'Giz',1.25,
            'Papel Sulfite 500f',31.75,
            'Cartolina',1.25,
            'Tesoura',6.5
)
print(('====')*15)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print(('====')*15)

for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')