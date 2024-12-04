#Exercício Python #084 - Lista composta e análise de dados _> https://www.youtube.com/watch?v=zPtvuLiEdKk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=16

print(('==*==')*20)
print('Bem vindo(a) - Lista composta e análise de dados ')
print(('==*==')*20)

pessoas = []
pesMaior = []
pesMenor = []
contador = 0
maiorPeso = menorPeso = soma = 0

while True:
    pessoas.append([input('Nome: '),float(input('Peso: '))])
    if pessoas[contador][1] < 0:
         break
    else:         
        if pessoas[contador][1] > maiorPeso:
            maiorPeso = pessoas[contador][1]
            pesMaior.clear()
            if menorPeso == 0:
                menorPeso = pessoas[contador][1]
                pesMenor.append(pessoas[contador][0])
            pesMaior.append(pessoas[contador][0]) 
        elif pessoas[contador][1] == maiorPeso:
            pesMaior.append(pessoas[contador][0])
            if pessoas[contador][1] == menorPeso:
                pesMenor.append(pessoas[contador][0])
        elif pessoas[contador][1] == menorPeso:
            pesMenor.append(pessoas[contador][0])
        elif pessoas[contador][1] < menorPeso:
            menorPeso = pessoas[contador][1]
            pesMenor.clear()
            pesMenor.append(pessoas[contador][0])
        
    soma += pessoas[contador][1]
    contador +=1
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
         continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
         break
print()
print(f'Ao todo, você cadastrou: {len(pessoas)} pessoas, são elas: {pessoas}.')
print(f'O maior peso foi de: {maiorPeso:.2f}. Peso de: {pesMaior}')
print(f'O menor peso foi de: {menorPeso:.2f}. Peso de: {pesMenor}')
print(f'O média de peso foi: {(soma/contador):.2f}')
