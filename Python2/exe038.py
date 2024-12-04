#Exercicio 38 - Comparador de números -> https://www.youtube.com/watch?v=iuPbB9uHczM&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=5

print(('==*==')*20)
print('Bem vindo(a) - Comparador de Números')
print(('==*==')*20)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f"{n1} é maior que {n2}")
elif n1 < n2:
    print(f"{n2} é maior que {n1}")
else:
    print(f"Não existe maior, {n1} e {n2} são iguais!")