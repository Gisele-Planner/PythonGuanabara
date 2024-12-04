#Exercício Python #080 - Lista ordenada sem repetições -> https://www.youtube.com/watch?v=QDpwjBYRcVE&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=11

print(('==*==')*20)
print('Bem vindo(a) - Lista ordenada sem repetições')
print(('==*==')*20)

#solução final
listagem = []
for c in range(0,5):
    número = int(input('Digite um número: '))
    if c == 0 or número > listagem[-1]:
        listagem.append(número)
        print(f'Inserido no final da lista')
    else:
        pos=0
        while pos < len(listagem):
            if número <= listagem[pos]:
                listagem.insert(pos,número)
                print(f'Inserido na posição {pos}')
                break
            pos +=1
print(('==*==')*20)
print(f'Você digitou os valores: {listagem}!')

    
#rascunho

# listagem = []
# contador = 1
# soma = 0

# while contador <= 5 :
#     número = int(input('Digite um número: '))
#     while número in listagem:
#          print('Esse número já tem na lista')
#          número = int(input('Digite outro número: '))
#     listagem.append(número)
#     print('Valor adicionado com sucesso!')
#     contador +=1
#     soma += número
# listagemOrdernada = listagem.sort()
# print()
# print(f'Você digitou os valores: {listagem}!')
# print(f'A soma dos itens digitados é: {soma}!')