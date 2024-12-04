#Exercício Python #055 - Maior e menor da sequência -> https://youtube.com/watch?v=Kjpb_IAOKRQ&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=23

print(('\033[30m==*==')*20)
print('Bem vindo(a) ao maior e menor de uma sequência de pesos')
print(('==*==')*20)

#Bibliotecas
from datetime import date 
from time import sleep

#Variaveis
pessoas = []

for p in range(1,6):
    peso = float(input(f"Digite o peso da {p}ª pessoa: "))
    pessoas.append(peso)

print('Processando..')
sleep(1)    

print(f"Neste grupo de {len(pessoas)} pessoas, o maior peso lido foi de: {(max(pessoas)):.1f} KG e o menor: {(min(pessoas)):.1f} KG")

