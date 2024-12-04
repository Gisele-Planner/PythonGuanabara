# Exercicio 31 - Distância Viagem -> https://www.youtube.com/watch?v=PGqHyzWoagc&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=32&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Distância Viagem')
print(('==*==')*20)

distancia = float(input("Digite uma distância em KM: "))
if distancia <=200:
    print(f"Para esta viagem de {distancia} KMs, irei te cobrar R$ {(distancia*0.50):.2f}")
else:
    print(f"Para esta viagem de {distancia} KMs, irei te cobrar R$ {(distancia*0.45):.2f}")