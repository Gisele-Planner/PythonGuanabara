#Exercício Python #075 - Análise de dados em uma Tupla -> https://www.youtube.com/watch?v=1u7oA8ckjAc&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=5

print(('==*==')*20)
print('Bem vindo(a) - Análise de dados em uma Tupla')
print(('==*==')*20)

números = (int(input('Digite um número: '))
           ,int(input('Digite outro número: '))
           ,int(input('Digite mais número: '))
           ,int(input('Digite o último número: ')))
pares = []
print(f'Você digitou os valoes: {números}')

print(f'O número 9 apareceu {números.count(9)} vezes')
if 3 in números:
    print(f"O número 3 apareceu {números.count(3)} vezes, na {(números.index(3))+1}ª posição.")
else:
    print("O número 3 não foi encontrado na lista.")
for e in números:
    if e % 2 == 0:
        pares.append(e)
print(f'Os valores pares digitados foram: {pares}')