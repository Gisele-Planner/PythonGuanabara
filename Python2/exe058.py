#Exercício Python #058 - Exercício Python #058 - Jogo da Adivinhação v2.0-> https://www.youtube.com/watch?v=-QkOIHJ1Chw&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=27

from random import randint

print(('\033[30m==*==')*20)
print('Bem vindo(a) ao ogo de adivinhação v2.0')
print(('==*==')*20)

print('\nAcabei de pensar em um número entre 0 e 10')

número = int(input('Em que número eu pensei? '))
computador = randint(0,10)
palpites = 1

while número != computador:
    if número > computador:
        print('Menos..tente mais uma vez')
        número = int(input('Qual seu palpite? '))
        palpites += 1
    else:
        print('Mais..tente mais uma vez')
        número = int(input('Qual seu palpite? '))
        palpites += 1
print(f'Parabéns, você adivinhou! com {palpites} palpites')