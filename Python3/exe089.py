#Exercício Python #089 - Boletim com listas compostas -> https://www.youtube.com/watch?v=7xrCJnniqMw&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=21

print(('==*==')*20)
print('Bem vindo(a) - Boletim com listas compostas')
print(('==*==')*20)

alunos = alunosResumo = []
contador = 0
while True:
    alunosTemp = []
    resumoTemp = []
    while True:
        nome = input('Nome: ')
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        alunoMedia = (nota1+nota2)/2
        contador += 1
        alunosTemp.append([nome,nota1,nota2,alunoMedia])
        resumoTemp.append([nome,alunoMedia])
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
        while continuar not in 'SN':
            continuar = input('Deseja continuar? [S/N]: ').strip().upper()
        if continuar == 'N':
            break
    alunos.append(alunosTemp)
    alunosResumo.append(resumoTemp)
    break

print(('==*==')*20)
print(f'{"No.":<4}{"NOME":<20}{"MÉDIA":>8}')
for p,i in enumerate(alunosResumo[0]):
    if p % 2 == 0:      
        print(f'{p:<4} {i[0]:.<20}', end ='')
        print(f'{i[1]:8.1f}')
    else:
        print(f'{p:<4} {i[0]:.<20}', end ='')
        print(f'{i[1]:8.1f}')
print(('==*==')*20)
print()
while True:
    mostrarNotas = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if mostrarNotas != 999:
        if mostrarNotas < contador:
            print()
            print(f'As notas de {alunos[0][mostrarNotas][0]} São: {alunos[0][mostrarNotas][1]},{alunos[0][mostrarNotas][2]}')
            print()
        else:
            print('Opção Inválida!')            
    else:
        break