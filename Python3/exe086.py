#Exercício Python #086 - Matriz em Python - https://www.youtube.com/watch?v=EGmlFdwD4C4&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=18

print(('==*==')*20)
print('Bem vindo(a) - Matriz em Python')
print(('==*==')*20)

numeros = []
for e in range(0,3):
    temp = []
    for i in range(0,3):
        número = int(input(f'Digite um valor para [{e},{i} ]: '))
        temp.append(número)
    numeros.append(temp)
for p,i in enumerate(numeros):
    print(f'{numeros[p]}')
    