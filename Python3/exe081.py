#Exercício Python #081 - Extraindo dados de uma Lista -> https://www.youtube.com/watch?v=SXJKAVVlvGA&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=12

print(('==*==')*20)
print('Bem vindo(a) - Extraindo dados de uma Lista')
print(('==*==')*20)


listagem = []
contador = 0
soma = 0

while True:
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
print()
print(f'Você digitou {contador} elementos, são eles, em ordem descrescente: {sorted(listagem,reverse=True)}!')
print(f'A soma dos itens digitados é: {soma}!')
if 5 in listagem:
     print(f'O valor 5 foi encontrado na lista!')
else:
     print(f'O valor 5 não foi encontrado na lista!!')
    