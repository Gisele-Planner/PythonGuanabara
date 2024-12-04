# Exercicio 29 - Radar -> https://www.youtube.com/watch?v=hgJ_ETNGSj8&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=30&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Radar')
print(('==*==')*20)

velocidade = int(input("Digite a velocidade do carro: "))
multaKm = 7
if velocidade > 80:
    print(f'Atenção! Você foi ultrapassou o limite de velocidade e foi multado em R$ {((velocidade-80)*multaKm):.2f}')
else:
    print(f'Siga em frente pequeno gafanhoto!')