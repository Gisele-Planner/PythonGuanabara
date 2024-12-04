#Exercício Python #063 - Sequência de Fibonacci v1.0 -> https://www.youtube.com/watch?v=w7yn1_Mfu0E
from time import sleep

print(('==*==')*20)
print('Bem vindo(a) a Sequência de Fibonacci v1.0')
print(('==*==')*20)

t1 = 0
t2 = 1
contador = 3
termos = int(input('Quantos termos você quer mostrar? '))
print(f'{t1} -> {t2} -> ', end = '')
while contador <= termos:
    t3 = t1+t2
    contador += 1
    print(f'{t3} -> ', end = '')
    t1 = t2
    t2 = t3
print("FIM")

    
   