#exercicio 083 - Exercício Python #083 - Validando expressões matemáticas - https://www.youtube.com/watch?v=dvhP41Z7TLk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=14

print(('==*==')*20)
print('Bem vindo(a) - Exercício Python #083 - Validando expressões matemáticas')
print(('==*==')*20)

parenteses = []
expressao = input('Digite a expressão: ').strip().upper()

for pos, letra in enumerate(expressao):
    if letra == '(':
        parenteses.append('(')  
    if letra == ')':
        parenteses.remove('(')
# print(f'A lista de parenteses = {parenteses}. Tamanho: {len(parenteses)}')
if len(parenteses) == 0:
    print('Sua Expressão está correta')
else:
    print('Sua Expressão está errada')