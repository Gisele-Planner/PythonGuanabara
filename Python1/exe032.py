# Exercicio 32 - Ano Bissexto -> https://www.youtube.com/watch?v=cyGY_83m4Xw&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=33&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Cálculo de Ano Bissexto')
print(('==*==')*20)

from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 100 == 0 and ano % 4 == 0:
    print(f'O ano de {ano} é bissexto')
elif ano % 100 == 0 and ano % 4 != 0:
    print(f'O ano de {ano} não é bissexto')
elif ano % 4 == 0:
    print(f'O ano de {ano} é bissexto')
elif ano % 4 != 0:
    print(f'O ano de {ano} não é bissexto')