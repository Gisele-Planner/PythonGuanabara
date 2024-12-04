#Exercício Python #078 - Maior e Menor valores na Lista -> https://www.youtube.com/watch?v=q8Z1cRdJnfk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=9

print(('==*==')*20)
print('Bem vindo(a) - Maior e Menor valores na Lista.')
print(('==*==')*20)

listagem = (int(input('Digite um valor para posição 0: ')),int(input('Digite um valor para posição 1: '))
            ,int(input('Digite um valor para posição 2: ')),int(input('Digite um valor para posição 3: '))
            ,int(input('Digite um valor para posição 4: ')),)
print(('====')*20)
print(f"Você digitou os valores: {listagem}")
print(f"O Maior valor foi: {max(listagem)} nas posições..", end = ' ')
for c, p in enumerate(listagem):
    if p == max(listagem):
        print(f'{c}',end = '..')
print(f"\nO Menor valor foi: {min(listagem)} nas posições..", end = ' ')
for c, p in enumerate(listagem):
    if p == min(listagem):
        print(f'{c}',end = '..')
