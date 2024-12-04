#Exercicio 15 - Aluguel de Carros -> https://www.youtube.com/watch?v=I4NYUeetLAc&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=16&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Aluguel de Carros')
print(('==*==')*20)

km = float(input("Digite quantos Km foram percorridos: "))
dias = int(input("Digite quantos dias ficou com o carro: "))
diariaCarro = 60
kmRodado = 0.15
print(f"O valor a pagar é de R$ {(dias*diariaCarro)+(km*kmRodado):.2f}, sendo: {(dias*diariaCarro):.2f} pelas diárias + {(km*kmRodado):.2f} pelos KMs rodados")