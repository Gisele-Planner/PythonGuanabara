#Exercicio 018 - Calculando seno, cosseno e tangente -> https://www.youtube.com/watch?v=9GvsphwW26k&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=19&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Cálculo de Seno, Cosseno e Tangente')
print(('==*==')*20)

import math
angulo = int(input("Digite um ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"O ângulo de {angulo}º tem o SENO de {seno:.2f}")
print(f"O ângulo de {angulo}º tem o COSSENO de {cosseno:.2f}")
print(f"O ângulo de {angulo}º tem a TANGENTE de {tangente:.2f}")

#radians é importante pois, não podemos jogar o angulo direto, precisamos do radiano.