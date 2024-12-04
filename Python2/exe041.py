#Exercicio 041 - Classificando Atletas -> https://www.youtube.com/watch?v=ZiC5NgSGJXU&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=8

print(('==*==')*20)
print('Bem vindo(a) ao seletor de categorias para natação de nossa escola ABC')
print(('==*==')*20)

from datetime import date 
from time import sleep

ano = int(input("Ano de Nascimento: "))
print('Processando..')
sleep(1)
anoAtual = date.today().year
idade = (anoAtual-ano)
if idade < 9:
    print(f"Você tem {idade} anos, Para natação, sua categoria é MIRIM")
elif idade >= 9 and idade < 14:
    print(f"Você tem {idade} anos, Para natação, sua categoria é INFANTIL")
elif idade >= 14 and idade < 19:
    print(f"Você tem {idade} anos, Para natação, sua categoria é JUNIOR")
elif idade >= 19 and idade < 25:
    print(f"Você tem {idade} anos, Para natação, sua categoria é SÊNIOR")
else:
    print(f"Você tem {idade} anos, Para natação, sua categoria é MASTER")