#Exercício Python #045 - GAME: Pedra Papel e Tesoura -> https://www.youtube.com/watch?v=tapTa6KVG-A&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=12
from time import sleep
from random import randint

print(('==*==')*20)
print('Bem vindo(a) ao Jokenpô')
print(('==*==')*20)

print(
    '''Suas opções:
    [ 1 ] PEDRA
    [ 2 ] PAPEL
    [ 3 ] TESOURA
'''
)
opcao = int(input("Qual é a sua jogada: "))
computador = randint(1,3)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print(('==*==')*10)


"""Regras: A pedra ganha da tesoura, o papel ganha da pedra, e a tesoura ganha do papel; 
Pedra empata com pedra, tesoura empata com tesoura, e papel empata com papel; """

if opcao == computador:
    print(f"EMPATE")
    if opcao == 1:
        print(f"Computador e Jogador jogaram PEDRA")
    elif opcao == 2:
        print(f"Computador e Jogador jogaram PAPEL")
    else:
        print(f"Computador e Jogador jogaram TESOURA")
elif opcao == 1 and computador == 2:
    print(f"Computador jogou PAPEL")
    print(f"Jogador jogou PEDRA")
    print(('==*==')*10)
    print(f"COMPUTADOR VENCE")
elif opcao == 1 and computador == 3:
    print(f"Computador jogou TESOURA")
    print(f"Jogador jogou PEDRA")
    print(('==*==')*10)
    print(f"JOGADOR VENCE")
elif opcao == 2 and computador == 1:
    print(f"Computador jogou PEDRA")
    print(f"Jogador jogou PAPEL")
    print(('==*==')*10)
    print(f"JOGADOR VENCE")
elif opcao == 2 and computador == 3:
    print(f"Computador jogou TESOURA")
    print(f"Jogador jogou PAPEL")
    print(('==*==')*10)
    print(f"COMPUTADOR VENCE")
elif opcao == 3 and computador == 2:
    print(f"Computador jogou PAPEL")
    print(f"Jogador jogou TESOURA")
    print(('==*==')*10)
    print(f"JOGADOR VENCE")
elif opcao == 3 and computador == 1:
    print(f"Computador jogou PEDRA")
    print(f"Jogador jogou TESOURA")
    print(('==*==')*10)
    print(f"COMPUTADOR VENCE")
else:
    print(f"Opção Inválida")
print(('==*==')*10)