# Exercicio 026 - Analisador de Textos, digite uma frase e conte letras -> https://www.youtube.com/watch?v=23UOVEetNPY&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=27&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Analisador de Textos - Busca em Frases')
print(('==*==')*20)

frase = input("Digite uma frase: ").lower().strip()
print(f"A letra A aparece {frase.count('a')} vezes na frase")
print(f"A primeira letra A apareceu na posição {frase.find('a')+1}")
print(f"A última letra A apareceu na posição {frase.rfind('a')+1}")
