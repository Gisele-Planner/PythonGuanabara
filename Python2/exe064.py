#Exercício Python #064 - Tratando vários valores v1.0 -> https://www.youtube.com/watch?v=mYlbttiLHM0
from time import sleep

print(('==*==')*20)
print('Bem vindo(a) - Tratando vários valores v1.0')
print(('==*==')*20)

soma = 0
contagem = 0
número = int(input('Digite um número [999 para parar]: '))
controle = 999
while número != controle:
    soma += número
    contagem += 1
    número = int(input('Digite um número [999 para parar]: '))
print(f"Você digitou {contagem} números e a soma entre eles foi: {soma:.2f}")
