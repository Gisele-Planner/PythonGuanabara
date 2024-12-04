#Exercício Python #082 - Dividindo valores em várias listas - https://www.youtube.com/watch?v=uk0gDFQEo_I&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=13

print(('==*==')*20)
print('Bem vindo(a) - Dividindo valores em várias listas')
print(('==*==')*20)

listagem = []
pares = []
impares = []
contador = 0
soma = 0

while True:
    listagem.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
         continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
         break
for e in listagem:
     if e % 2 == 0:
          pares.append(e)
     else:
          impares.append(e)
print()
print(f'A lista completa é {listagem}!')
print(f'A lista de pares é: {pares}!')
print(f'A lista de impares é: {impares}!')
