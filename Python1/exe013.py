#Exercicio 13 - Reajuste Salárial -> https://www.youtube.com/watch?v=cTkivN8XcJ0&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=14&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Calculo de Reajuste Salárial')
print(('==*==')*20)

salarioAtual = float(input("Digite o valor do seu salário atual: R$ "))
aumento = 0.15
novoSalario = salarioAtual*(1+aumento)
print(f"Com o aumento salarial de {aumento*100}%, o seu salário anterior de R$ {salarioAtual:.2f} vai para R$ {novoSalario:.2f}")