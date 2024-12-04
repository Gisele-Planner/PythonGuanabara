#Exercício Python #054 - Grupo da Maioridade -> https://www.youtube.com/watch?v=IL5iBWoKRIs&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=22

print(('\033[30m==*==')*20)
print('Bem vindo(a) ao Validador de Grupos De Maioridade')
print(('==*==')*20)

#Bibliotecas
from datetime import date 
from time import sleep

#Variaveis
pessoas = []
menores = 0
maiores = 0
anoAtual = date.today().year

for p in range(1,8):
    anoNascimento = int(input(f"Em que ano a {p}ª pessoa nasceu? "))
    pessoas.append(anoNascimento)
    if anoAtual - anoNascimento < 21:
        menores += 1
    else:
        maiores += 1

print('Processando..')
sleep(2)    
print(f"Neste grupo de {len(pessoas)} pessoas, {menores} são menores de idade e {maiores} maiores")

