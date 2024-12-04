#Exercício Python #061 - Progressão Aritmética -> https://www.youtube.com/watch?v=-OnqSGh0u4g&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=19
from time import sleep

print(('==*==')*20)
print('Bem vindo(a) a Progressão Aritmética V2.0')
print(('==*==')*20)

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
qtdeTermos = 10
contador = 1
soma = primeiroTermo
print(f'{primeiroTermo}',end = ' -> ')

while contador < qtdeTermos:
    soma += razao
    contador += 1
    print(f'{soma}',end = ' -> ')

print('FIMMMM')