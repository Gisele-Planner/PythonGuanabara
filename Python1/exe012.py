#Exercicio 12 - Calculando descontos -> https://www.youtube.com/watch?v=4MAmKOT9FeU&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=13&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Calculo de Descontos')
print(('==*==')*20)

precoAnterior = float(input("Digite o valor do seu produto: R$"))
desconto = 0.05
precoAtual = precoAnterior*(1-desconto)
print(f"Com o desconto de {desconto*100}%, o produto sai de R$ {precoAnterior:.2f} para R$ {precoAtual:.2f}")