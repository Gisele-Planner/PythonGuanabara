#Exercicio 10 - Conversão de Moedas -> https://www.youtube.com/watch?v=xM4AX3Lp2mo&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=11&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) Sistema de Conversão de Moedas')
print(('==*==')*20)

real = float(input("Digite quantos R$ você tem na carteira: "))
dolar = 5.60

print(f"Com seus R${real:.2f}, você pode comprar U$${(real/dolar):.2f}")
