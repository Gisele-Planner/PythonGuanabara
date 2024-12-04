#exercicio 079 - Exercício Python #079 - Valores únicos em uma Lista

print(('==*==')*20)
print('Bem vindo(a) - Valores únicos em uma Lista')
print(('==*==')*20)

listagem = []
contador = 0
soma = 0

while True:
    número = int(input('Digite um número: '))
    while número in listagem:
         print('Esse número já tem na lista')
         número = int(input('Digite um número: '))
    listagem.append(número)
    print('Valor adicionado com sucesso!')
    contador +=1
    soma += número
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
         continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
         break
listagemOrdernada = listagem.sort()
print()
print(f'Você digitou {contador} valores únicos, são eles: {listagem}!')
print(f'A soma dos itens digitados é: {soma}!')