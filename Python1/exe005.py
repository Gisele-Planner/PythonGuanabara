#Exercicio 05 - Antes e Depois de um número inteiro -> https://www.youtube.com/watch?v=664e0G_S9nU&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=5&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a)!')
print(('==*==')*20)

número = int(input("Digite um número inteiro inteiro: "))
if número % 1 == 0:
    print(f"O antecessor de {número} é {número-1} e o sucessor é {número+1}")
else:
    print("Você não digitou um número inteiro!")