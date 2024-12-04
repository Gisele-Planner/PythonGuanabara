#Exercicio 43 - Índice de Massa Corporal - https://www.youtube.com/watch?v=b7r34za963I&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=10

print(('==*==')*20)
print('Bem vindo(a) ao sistema de cálculo de índice de massa corporal (IMC)')
print(('==*==')*20)

peso = float(input("Digite o seu peso (KG): "))
altura = float(input("Digite sua altura (M): "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Com o IMC de {imc:.2f}, Você está abaixo do peso normal')
elif imc >= 18.5 and imc <  25:
    print(f'Com o IMC de {imc:.2}, Parabéns! Você está no peso ideal')
elif imc >= 25.5 and imc <  30:
    print(f'Com o IMC de {imc:.2f}, Cuidado! Você está com Sobrepeso')
elif imc >= 30 and imc <  40:
    print(f'Com o IMC de {imc:.2f}, Você está com Sobrepeso, não deixe de procurar ajuda')
else:
    print(f'Com o IMC de {imc:.2f}, Você está com Obesidade mórbida, procure ajuda!')