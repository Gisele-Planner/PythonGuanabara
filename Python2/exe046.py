#Exercício Python #046 - Contagem regressiva -> https://www.youtube.com/watch?v=NR1RKt6NT8s
from time import sleep

print(('==*==')*20)
print('Bem vindo(a) a contagem regressiva')
print(('==*==')*20)

for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('Fogo!')