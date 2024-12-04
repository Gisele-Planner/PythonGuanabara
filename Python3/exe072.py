#exercicio 072 - Exercício Python #072 - Número por Extenso -> https://www.youtube.com/watch?v=ei2Kr3ccfO0&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=2

print(('==*==')*20)
print('Bem vindo(a) - Número por Extenso')
print(('==*==')*20)

numerosExtenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while True:
    número = int(input("Digite um número entre 0 e 20: "))
    if número >= 0 and número <= 20:
        print(f'você digitou o número {numerosExtenso[número]}')
        break
    else:
        número = int(input("Digite um número entre 0 e 20: "))