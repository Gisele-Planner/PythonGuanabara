#Exercício Python #092 - Cadastro de Trabalhador em Python -> https://www.youtube.com/watch?v=Vsqemzdrj78&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=25

print(('==*==')*20)
print('Cadastro de Trabalhador em Python ')
print(('==*==')*20)

from datetime import date
anoAtual = date.today().year

trabalhador = {}
trabalhador['nome'] = input("Nome: ")
trabalhador['ano de nascimento']= int(input("Ano de Nascimento: "))
trabalhador['idade'] = anoAtual - trabalhador['ano de nascimento']
trabalhador['carteira de trabalho']= int(input("Carteira de Trabalho (0 não tem): "))
if trabalhador['carteira de trabalho'] != 0:
    trabalhador['ano contratação']= int(input("Ano de Contratação: "))
    trabalhador['salário']= float(input("Salário: "))
    trabalhador['Aposentadoria'] = (trabalhador['ano contratação']+35)-trabalhador['ano de nascimento']
    print(('==*==')*20)
    for k, v in trabalhador.items():
        print(f'- {k} : {v}')
else:
    print(('==*==')*20)
    for k, v in trabalhador.items():
        print(f'- {k} : {v}')
print()