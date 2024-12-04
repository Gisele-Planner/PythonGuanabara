#Exercício Python #064 - Tratando vários valores v1.0 -> https://www.youtube.com/watch?v=mYlbttiLHM0
from time import sleep

print(('==*==')*20)
print('Bem vindo(a) - Tratando vários valores v1.0')
print(('==*==')*20)

soma = 0
contagem = 0
valores = []

while True:
    número = int(input('Digite um número [999 para parar]: '))
    if número == 999:
        break
    soma += número  
    valores.append(número)
    contagem += 1
print(f"Você digitou {contagem} números e a soma entre eles foi: {soma:.2f}")
print(f"A média foi: {(soma/contagem):.2f}")
print(f"A maior foi: {(max(valores)):.2f} e o menor: {(min(valores)):.2f} ")