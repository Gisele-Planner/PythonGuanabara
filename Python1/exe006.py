#Exercicio 06 - Crie um algoritimo de leia um número e mostre o seu dobro, triplo e a raiz quadrada -> https://www.youtube.com/watch?v=mqcNw_dhl8I&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=7&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) Sistema de cálculo de  Dobro | Triplo | Raiz Quadrada')
print(('==*==')*20)

número = int(input("Digite um número inteiro: "))
dobro = número * 2
triplo = número * 3
raiz = número ** (1/2) #como calcular a raiz quadrada
print(f"O dobro de {número} é: {dobro}, o triplo é: {triplo} e a raiz quadrada é: {raiz:.2f}")
