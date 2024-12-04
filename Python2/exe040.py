#Exercicio 040 - Média Escolar -> https://www.youtube.com/watch?v=QuWDyUeoaJs&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=7

print(('==*==')*20)
print('Bem vindo(a) - Média Escolar')
print(('==*==')*20)

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = (nota1+nota2)/2
if media < 5:
    print(f"Reprovado. Sua média foi de {media:.2f}")
elif media >= 5 and media < 6.9:
     print(f"Recuperação. Sua média foi de {media:.2f}")
else:
     print(f"Aprovado! Sua média foi de {media:.2f}")