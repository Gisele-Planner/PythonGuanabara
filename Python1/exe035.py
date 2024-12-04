# Exercicio 35 - calculo de um triangulo -> https://www.youtube.com/watch?v=NZiNphKkxhg&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=36

print(('==*==')*20)
print('Bem vindo(a) - Existência de um Triangulo')
print(('==*==')*20)

# |b – c| < a < b + c
m1 = float(input("Digite a medida 1: "))
m2 = float(input("Digite a medida 2: "))
m3 = float(input("Digite a medida 3: "))
if abs(m2 - m3) < m1 < m2 + m3: #abs é a formula de módulo
    print("É possível formar um triângulo")
else:
    print("Não é possível formar um triângulo")
