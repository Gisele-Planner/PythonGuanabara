#Exercicio 016 -> Quebrando número - > https://www.youtube.com/watch?v=-iSbDpl5Jhw&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=17&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Quebrando Número')
print(('==*==')*20)

from math import trunc # Importando a biblioteca Math e utilizando o método trunc, que traz somente a parte inteira
num = float(input("Digite um número: "))
print(f"O número {num:.2f} tem a parte inteira {trunc(num)}")
