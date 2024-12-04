# Exercicio 28 - Jogo de adivinhação -> https://www.youtube.com/watch?v=kchC5KLZSZ4&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=29&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Jogo de Adivinhação')
print(('==*==')*20)

print('\nBem vindo ao jogo de adivinhação v1.0 \n')
print('Vou pensar em um número entre 0 e 5')
número = int(input('Em que número eu pensei? '))
print('Processando...')
if número >= 0 and número <=5:
    import random
    computador = random.randint(0,5)
    if número == computador:
        print('Parabéns, você adivinhou!')
    else:
        print(f'Sinto muito, você errou, o número que pensei foi: {computador}')
else:
    print('Número inválido!')