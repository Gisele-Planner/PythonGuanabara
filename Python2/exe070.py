#Exercício Python #069 - Análise de dados do grupo -> https://www.youtube.com/watch?v=hS8QdW-1HTo&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=40

print(('==*==')*20)
print('Bem vindo(a) - Exercício Python #070 - Estatísticas em produtos')
print(('==*==')*20)
print('Lojão do Silva')
print(('==*==')*20)

contadorProdutos = 0
prodmais1000 = 0
valorCompra = 0
produtoBaratoValor = 0
produtoBaratoNome = ''

while True:
    produto = input('Nome do Produto: ').strip()
    preco = float(input('Preço: R$ '))
    contadorProdutos +=1
    valorCompra += preco
    if preco > 1000:
        prodmais1000 +=1
    if produtoBaratoValor == 0:
        produtoBaratoValor = preco
        produtoBaratoNome = produto
    elif preco < produtoBaratoValor and preco !=0:
        produtoBaratoValor = preco
        produtoBaratoNome = produto
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    while continuar not in 'SsNn':
        print('Opção Inválida')
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar in 'Nn':
        break
print(('\n=====Fim do Programa====='))
print(f'\nTotal da compra: {valorCompra:.2f}')
print(f'Total de Produtos: {contadorProdutos}')
print(f'Produtos acima de RS 1.000: {prodmais1000}')
print(f'Produto mais barato: {produtoBaratoNome} que custa R$ {produtoBaratoValor:.2f}')