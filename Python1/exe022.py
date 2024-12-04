# Exercicio 22 - Analisador de Textos -> https://www.youtube.com/watch?v=EQQt-6QqXOs&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=23&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Analisador de Textos')
print(('==*==')*20)

nome = input("Digite seu nome completo: ").strip()
print(f"Analisando o seu nome..")
print(f"{nome.upper()} em Maíusculo")
print(f"{nome.lower()} em mínusculo")
separa = nome.split()
print(f"{len(nome)-nome.count(' ')} letras no total")
print(f"seu primeiro nome é {separa[0]}e ele tem {len(separa[0])} letras")

