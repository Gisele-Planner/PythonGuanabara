#Exercicio 37 - Conversor de bases númericas -> https://www.youtube.com/watch?v=B3F0IjH5WAM&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=4

print(('==*==')*20)
print('Bem vindo(a) - Conversor de Bases')
print(('==*==')*20)

n = int(input("Digite um número inteiro: "))
print(
    '''Escolha uma das bases para conversão:
    [ 1 ] converter para binário
    [ 2 ] converter para octal
    [ 3 ] converter para hexadecimal
'''
)
opcao = int(input("Sua opção: "))
if opcao == 1:
    print(f"{n} convertido para Binário é igual a {(bin(n)[2:])}")
elif opcao == 2:
    print(f"{n} convertido para Octal é igual a {(oct(n)[2:])}")
elif opcao == 3:
    print(f"{n} convertido para Hexadecimal é igual a {(hex(n))}")
else:
    print(f"Opção Inválida")