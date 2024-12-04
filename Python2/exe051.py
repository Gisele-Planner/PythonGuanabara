#Exercício Python #051 - Progressão Aritmética -> https://www.youtube.com/watch?v=-OnqSGh0u4g&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=19
from time import sleep

print(('==*==')*20)
print('Bem vindo(a) a Progressão Aritmética')
print(('==*==')*20)

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
qtdeTermos = 10
limite = primeiroTermo + qtdeTermos * razao 

for c in range(primeiroTermo,limite,razao):
    print(f'{c}',end = ' -> ')
print(f'Acabou.')  
print(f'Estes são os {qtdeTermos} primeiros números, somados de {razao} a partir de {primeiroTermo}.')  