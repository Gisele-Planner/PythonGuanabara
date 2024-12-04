# Exercicio 30 - Par/Impar -> https://www.youtube.com/watch?v=4vFCzKuHOn4&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=31&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Par ou Impar')
print(('==*==')*20)

num = float(input("Digite um número: "))
if num % 2 == 0:
    print(f"O número {num:.2f} é PAR!")
else:
    print(f"O número {num:.2f} é Impar!")