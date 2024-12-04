#Exercício Python #064 - Tratando vários valores v1.0 -> https://www.youtube.com/watch?v=mYlbttiLHM0
from time import sleep

print(('==*==')*20)
print('Bem vindo(a) - Exercício Python #065 - Maior e Menor valores')
print(('==*==')*20)

soma = 0
contagem = 0
número = int(input('Digite um número: '))
controle = 1
valores = []
while controle >= 1:
    soma += número
    contagem += 1
    valores.append(número)
    continuar = input('Quer Continuar? [S/N]: ').strip().upper()
    if continuar in 'Ss':
        número = int(input('\nDigite um número: '))
    elif continuar in 'Nn':
        controle -= 1
    else:
        print('Opção inválida')
        controle -= 1

print(f"\nVocê digitou {contagem} números, somados {soma:.2f} e a média entre eles foi: {(soma/contagem):.2f}")
print(f"O maior valor foi {(max(valores))} e o menor foi: {(min(valores))}")
print('\nFim')

