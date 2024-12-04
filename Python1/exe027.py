# Exercicio 27 - Analisador de Textos, digite seu nome completo -> https://www.youtube.com/watch?v=SifYYsXhLM8&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=28&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Analisador de Textos - Nome Completo')
print(('==*==')*20)

nome = input("Digite uma nome completo: ").strip()
print('Muito Prazer em te conhecer!')
print(f'Seu primeiro nome é {nome.split()[0]}')
print(f'Seu último nome é {nome.split()[-1]}')