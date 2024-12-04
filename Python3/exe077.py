#exercicio 077 - Contando vogais em Tupla -> https://www.youtube.com/watch?v=8BgSqrOpKvU&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=7

print(('==*==')*20)
print('Bem vindo(a) - Contando vogais em Tupla')
print(('==*==')*20)

listagem = ("FACULDADE","QUALIDADE","ENSINO","APRENDIZADO","DEDICACAO","ESFORCO","CRESCIMENTO")

for pos in listagem:
    print(f'\nNa palavra {pos.upper()} temos: ',end = '')
    for letra in pos:
        if letra in 'AEIOUaeiou':
            print(f'{letra.lower()}',end = ' ')