#Exercício Python #069 - Análise de dados do grupo -> https://www.youtube.com/watch?v=4Ca6iRJo3M0&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=39

print(('==*==')*20)
print('Bem vindo(a) - Análise de dados do grupo')
print(('==*==')*20)


#Bibliotecas
from time import sleep

contagem = 0
maiores18 = 0
contagemHomens = 0
mulheresMenores20 = 0

while True:
    print(('====')*5)
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    if idade > 18:
        maiores18 += 1
    sexo = input('Sexo: [M/F] ').strip().upper()
    while sexo not in 'MmFf':
        print('Por favor, informe Sexo: [M/F] ')
        sexo = input('Sexo: [M/F] ').strip().upper()
    if sexo == 'M':
        contagemHomens += 1
    if sexo == 'F' and idade < 20:
         mulheresMenores20 += 1
    
    print(('====')*5)
    contagem += 1
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    while continuar not in 'SsNn':
        print('Opção Inválida')
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar in 'Nn':
        print('Fim')
        break
print(f'Foram cadastradas {contagem} pessoas')
print(f'Destas estão cadastradas {maiores18} maiores de 18 anos')
print(f'Ao todo {contagemHomens} homens cadastrados')
print(f'E temos {mulheresMenores20} mulheres abaixo de 20 anos')

