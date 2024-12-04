#Exercício Python #062 - Progressão Aritmética -> https://www.youtube.com/watch?v=-OnqSGh0u4g&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=19
from time import sleep

print(('==*==')*20)
print('Bem vindo(a) a Progressão Aritmética V3.0')
print(('==*==')*20)

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
qtdeTermos = 10
contador = 1
soma = primeiroTermo
termosTotal = qtdeTermos
controle = 1
print(f'{primeiroTermo}',end = ' -> ')

while controle > 0:
    while contador < termosTotal:
        soma += razao
        contador += 1
        print(f'{soma}',end = ' -> ')
    print('\n\n')
    novoTermo = int(input('Quantos termos quer mostrar a mais: '))
    if novoTermo != 0:
        termosTotal += novoTermo
    elif novoTermo == 0:
        controle -= 1
print(f'\nProgressão finalizada com {termosTotal} termos mostrados!')

    
   