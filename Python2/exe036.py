#Exercicio 36 - Simulação de empréstimo -> https://www.youtube.com/watch?v=IV13X0QOMU8&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=3

print(('==*==')*20)
print('Bem vindo(a) - Simulação de Empréstimo')
print(('==*==')*20)

valorCasa = float(input("Qual o valor do imóvel? R$ "))
salarioComprador = float(input("Qual o salário do comprador? R$ "))
anos = int(input("Em quantos anos pretende pagar este empréstimo? "))
meses = anos*12
limitePrestacao = salarioComprador*0.30
prestacao = (valorCasa/meses)
if prestacao <= limitePrestacao:
    print(f"Parabéns! Seu empréstimo foi aprovado, você pagará {meses}  x R$ {prestacao:.2f}")
else:
    print(f"Infelizmente, a parcela de R$ {prestacao:.2f} ultrapassa o limite de 30% de seu salário")