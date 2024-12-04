#Exercício Python #044 - Gerenciador de Pagamentos -> https://www.youtube.com/watch?v=I-SH3QchuZ4&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=11
from time import sleep

print(('==*==')*20)
print('Bem vindo(a) a nossa Mercearia SILVA')
print(('==*==')*20)

valorCompra = float(input("Digite o valor da sua compra: R$ "))
print(
    '''Escolha a forma de pagamento:
    [ 1 ] DINHEIRO/PIX (Desconto de 10%)
    [ 2 ] DÉBITO OU CRÉDITO 1X (Desconto de 5%)
    [ 3 ] CRÉDITO 2X (Sem juros)
    [ 4 ] CRÉDITO 3X ATÉ 10X (20% juros)
'''
)
opcao = int(input("Digte sua opção de pagamento: "))
if opcao == 1:
    print(f"Parabéns! você ganhou 10% de desconto, com isso, o valor a pagar é de R$ {(valorCompra*0.90):.2f}")
elif opcao == 2:
    print(f"Parabéns! você ganhou 5% de desconto, com isso, o valor a pagar é de R$ {(valorCompra*0.95):.2f}")
elif opcao == 3:
    print(f"O valor a pagar é de R$ {(valorCompra):.2f}, em 2X de R$ {(valorCompra/2):.2f}")
elif opcao == 4:
    parcelas = int(input("Em quantas parcelas: "))
    print('Processando..')
    sleep(1)
    if parcelas > 2 and parcelas <=10:
        print(f"O valor a pagar é R$ {(valorCompra):.2f}, em {parcelas} de R$ {((valorCompra*1.20)/parcelas):.2f}")
    else:
        print(f"Opção Inválida")
else:
    print(f"Opção Inválida, Tente novamente!")