#Exercício Python #057 - Validação de dados -> https://youtube.com/watch?v=Kjpb_IAOKRQ&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=23

print(('\033[30m==*==')*20)
print('Bem vindo(a) ao Validação de dados')
print(('==*==')*20)

sexo = input("Informe seu sexo (M/F):").strip().upper()[0]
while sexo not in 'MF':
    sexo = input("Dados inválidos, Por favor, Informe seu sexo (M/F):").strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')