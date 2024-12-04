#Exercício Python #056 - Analisador completo -> https://youtube.com/watch?v=Kjpb_IAOKRQ&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=23

print(('\033[30m==*==')*20)
print('Bem vindo(a) ao maior e menor de uma sequência de pesos')
print(('==*==')*20)

#Bibliotecas
from time import sleep

#Variaveis
somaIdade = 0
maiorIdadeHomem = 0
nomeHomem = ''
mulherMenor = 0
homens = 0
mulheres = 0

for p in range(1,5):
    print(f'{('-----'*5)} - {p}ª Pessoa {('-----'*5)}')
    nome = input("Nome: ")
    idade = int(input('Idade: '))
    somaIdade += idade
    sexo = input("Sexo (M/F): ").strip().upper()
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeHomem = nome
        homens += 1
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomem = nome 
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulherMenor += 1
        mulheres += 1

print('Processando..')
sleep(2)  
     
print(f'A média de idade do grupo é de {(somaIdade)/4:.2f}')
if homens >= 1:
    print(f"O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeHomem}")
print(f"Há {mulherMenor} mulheres menores que 20 anos no grupo ")

  

# print(f"Neste grupo de {len(pessoas)} pessoas, o maior peso lido foi de: {(max(pessoas)):.1f} KG e o menor: {(min(pessoas)):.1f} KG")

