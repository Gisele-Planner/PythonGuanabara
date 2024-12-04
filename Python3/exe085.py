#Exercício Python #085 - Listas com pares e ímpares -> https://www.youtube.com/watch?v=2-fy24bbMJ4&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=17


print(('==*==')*20)
print('Bem vindo(a) - Listas com pares e ímpares')
print(('==*==')*20)

numeros = [[],[]]

for e in range(1,8):
    numero = int(input(f'Digite o {e}º valor: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

numeros[0].sort()
numeros[1].sort()
print(f'Os números pares são: {numeros[0]}')
print(f'Os números impares são: {numeros[1]}')

#Alternativa para classificar
# for p,i in enumerate(numeros):
#     alinhado = i.sort()
#     if p ==0:
#         print(f'Os números pares são:{[i]}')
#     else:
#         print(f'Os números impares são:{[i]}')