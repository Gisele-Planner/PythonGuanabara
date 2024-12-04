#Exercicio 09 - Tabuada -> https://www.youtube.com/watch?v=qajq3SI0QQs&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=10&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) Sistema de Tabuada')
print(('==*==')*20)

número = int(input("Digite um número Inteiro: "))
sequencia = 1

while sequencia <= 10:
    print(f"{número} X {sequencia} = {número*sequencia}")
    sequencia +=1