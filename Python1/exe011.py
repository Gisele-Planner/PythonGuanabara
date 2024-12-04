#Exercicio 11 - Pintando Parede -> https://www.youtube.com/watch?v=mzSJpn9ldt4&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=12&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Calculo de Tinta para Pintura')
print(('==*==')*20)

largura = float(input("Digite em metros, a largura de sua parede: "))
altura = float(input("Digite em metros, a altura de sua parede: "))
area = largura*altura
rendimento = 2

print(f"Para uma parede de {largura:.2f} X {altura:.2f}, com área total de {area:.2f}m2, será necessário {(area/rendimento):.2f} litros de tinta")