#Exercício Python #059 - Criando um Menu de Opções-> https://www.youtube.com/watch?v=OBJL5vPj4-E&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=28

print(('\033[30m==*==')*20)
print('Bem vindo(a) ao Menu de Opções')
print(('==*==')*20)


número1 = float(input('Digite o primeiro valor: '))
número2 = float(input('Digite o segundo valor: '))
opcoes = '''
=-==-==-==-==-==-==-==-==-==-==-==-==
      [1] Somar
      [2] Multiplicar
      [3] Maior
      [4] Novos Números
      [5] Sair do programa
=-==-==-==-==-==-==-==-==-==-==-==-==
'''
print(opcoes)

opcao = int(input(">>> Digite sua opção: "))

while opcao < 5:
    if opcao == 1:
        print(f'A soma de {número1} + {número2} é: {(número1+número2)}')
        print(opcoes)
        opcao = int(input(">>> Digite sua opção: "))
    elif opcao == 2:
        print(f'A multiplicação de {número1} x {número2} é: {(número1*número2)}')
        print(opcoes)
        opcao = int(input(">>> Digite sua opção: "))
    elif opcao == 3:
        print(f'O maior número entre {número1} e {número2} é: {(max(número1,número2))}')
        print(opcoes)
        opcao = int(input(">>> Digite sua opção: "))
    elif opcao == 4:
        print('Perfeito, informe os novos números:')
        número1 = float(input('Digite o primeiro valor: '))
        número2 = float(input('Digite o segundo valor: '))
        print(opcoes)
        opcao = int(input(">>> Digite sua opção: "))
    
print('Fim')