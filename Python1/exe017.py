#Exercicio 017 - Calculando a hipotenusa -> https://www.youtube.com/watch?v=vmPW9iWsYkY&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=18&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Cálculo de Hipotenusa')
print(('==*==')*20)

ladoA = float(input("Digite o comprimento do Lado A: "))
ladoB = float(input("Digite o comprimento do Lado B: "))
ladoC2 = (ladoA*ladoA)+(ladoB*ladoB)
ladoC= ladoC2 ** 0.5
print(f"Sendo: lado A = {ladoA:.2f} + lado B = {ladoB:.2f}. O lado C é: {ladoC:.2f}")
