#exercicio 074 - Exercício Python #074 - Maior e menor valores em Tupla -> https://www.youtube.com/watch?v=mlwt2CRQkTQ&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=4

print(('==*==')*20)
print('Bem vindo(a) - Exercício Python #074 - Maior e menor valores em Tupla')
print(('==*==')*20)

from random import randint

tupla = [randint(1, 40) for a in range(5)]
print(f'Os itens sorteados foram: {(tupla)} Sendo: o menor: {min(tupla)} e o maior: {max(tupla)}')
print(f'Itens sorteados em ordem: {sorted(tupla)}')