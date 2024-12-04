# Exercicio 034 - Aumentos multiplos -> Link

print(('==*==')*20)
print('Bem vindo(a) - Aumento Salárial - Faixas')
print(('==*==')*20)

salario = float(input('Qual o seu salário: R$'))
if salario <= 1250:
    novoSalario = salario*1.15
    print(f'Parabéns! seu salário era R$ {salario:.2f} e com o aumento de 15%, agora será de: R$ {novoSalario:.2f}')
elif salario > 1250:
    novoSalario = salario*1.10
    print(f'Parabéns! seu salário era R$ {salario:.2f} e com o aumento de 10%, agora será de: R$ {novoSalario:.2f}')