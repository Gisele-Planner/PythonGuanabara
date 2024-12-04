#Exercicio 08 - Conversor de Medidas -> https://www.youtube.com/watch?v=KjcdG05EAZc&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=9&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) Sistema de cálculo de  Média')
print(('==*==')*20)

medida= float(input("Digite uma distância em metros: "))
centimetros = medida * 100
milimetros = medida * 1000
print(f"A medida de {medida:.2f} metros, corresponde a {centimetros:.2f} cm e {milimetros:.2f} mm")
