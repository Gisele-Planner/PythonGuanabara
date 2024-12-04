#Exercicio 042 - Analisando Triângulos v2.0 - https://www.youtube.com/watch?v=ZX7sCPjcHA0&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=9

print(('==*==')*20)
print('Bem vindo(a) ao seletor de Analise de Triângulos')
print(('==*==')*20)

# |b – c| < a < b + c #o módulo de B - C é menor que A que é menor que (B + C)

m1 = float(input("Digite a medida 1: "))
m2 = float(input("Digite a medida 2: "))
m3 = float(input("Digite a medida 3: "))
if abs(m2 - m3) < m1 < m2 + m3: #abs é a formula de módulo
    print("É possível..")
    if m1 != m2 and m1 != m3:
        print('Essas medidas formam um triângulo Escaleno!')
    elif m1 == m2 and m2 == m3:
        print('Essas medidas formam um triângulo Equilatéro!')
    else:
        print('Essas medidas formam um triângulo Isósceles!')
else:
    print("Não é possível formar um triângulo")

