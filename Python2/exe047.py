#Exercício Python #047 - Contagem de pares -> https://www.youtube.com/watch?v=Qws8-E-YrlY
from time import sleep

print(('==*==')*20)
print('Bem vindo(a) a Contagem de pares')
print(('==*==')*20)

print(('\nProcessando...'))
sleep(2)
listagem = []
for c in range(2,51,2):
    listagem.append(c)    
print(listagem)
print('Acabou')