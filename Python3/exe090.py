#Exercício Python #090 - Dicionário em Python -> https://www.youtube.com/watch?v=HipQYUk4koA&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=23

print(('==*==')*20)
print('Bem vindo(a) - Dicionário em Python')
print(('==*==')*20)

aluno = {}
aluno['nome'] = input("Nome: ")
aluno['média']= float(input("Média: "))
if aluno['média'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['média'] > 5 and aluno['média'] < 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(('==*==')*20)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
