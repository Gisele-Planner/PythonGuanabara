#Exercicio 49 - Tabuada -> https://www.youtube.com/watch?v=qajq3SI0QQs&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=10&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) Sistema de Tabuada V2.0')
print(('==*==')*20)

from time import sleep

número = int(input("Digite um número Inteiro para ver a Tabuada: "))
sequencia = 1
print(('\nProcessando...\n'))
sleep(1)
for c in range(0,10):
    print(f"{número} X {sequencia} = {número*sequencia}")
    sequencia += 1



