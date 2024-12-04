#Exercício Python #068 - Jogo do Par ou Ímpar -> https://www.youtube.com/watch?v=EIzgKCCDdc0&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=38

print(('==*==')*20)
print('Bem vindo(a) - Jogo do Par ou Ímpar')
print(('==*==')*20)
print(('\nVamos jogar PAR ou Ímpar'))
print(('==*==')*20)

from random import randint
from time import sleep

contagem = 0
jogadas = 0
while True:
    valorJogador = int(input('Digite um valor: '))
    escolha = input('Par ou Ímpar? [P/I]: ').strip().upper()
    jogadas += 1
    if escolha in 'PpIi':
        print(('\nProcessando...\n'))
        sleep(1)
        computador = randint(1,9)
        soma = valorJogador+computador
        if soma % 2 == 0 and escolha in 'Pp':
            print(f'Você jogou {valorJogador} e o Computador {computador}. Total de {soma:.2f} deu PAR!')
            print(f'Você VENCEU!')
            print(f'Vamos jogar novamente..')
            print(('==*==')*20)
            contagem += 1
        else:
            print(f'Você jogou {valorJogador} e o Computador {computador}. Total de {soma:.2f} deu Ímpar!')
            print(f'Você PERDEU!')
            break
    else:
        print(f'Opção Inválida')
        break
print(('==*==')*20)
print(f'GAME OVER! Você jogou {jogadas}X e venceu {contagem} vezes!')


