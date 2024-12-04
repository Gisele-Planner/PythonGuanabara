#Exercicio 039 - Alistamento militar -> https://www.youtube.com/watch?v=ePwP4gU_waY&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=6

print(('==*==')*20)
print('Bem vindo(a) - Alistamento Militar')
print(('==*==')*20)

ano = int(input("Ano de Nascimento: "))
from datetime import date
anoAtual = date.today().year
anoAlistamento = (ano+18)
idade = (anoAtual-ano)
if anoAlistamento == anoAtual:
    print(f"Você tem {idade} anos, chegou a sua vez, você deve se alistar imediatamente!")
elif anoAlistamento < anoAtual:
    print(f"Você tem {idade} anos, deveria se alistar em {anoAlistamento}. Se passaram {(anoAtual-anoAlistamento)} anos")
else:
    print(f"Você tem {idade} anos, só deve se alistar em {anoAlistamento}. Ainda Faltam {(anoAlistamento-anoAtual)} anos")