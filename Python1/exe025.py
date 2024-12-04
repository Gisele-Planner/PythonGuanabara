# Exercicio 25 - Analisador de Textos, precisa ter "silva" no nome -> https://www.youtube.com/watch?v=WHWGz2Dy1ZU&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=26&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Analisador de Textos - Parte de Texto')
print(('==*==')*20)

nome = input("Digite seu nome completo ").strip()
print(f"Seu nome tem Silva? {'Silva' in nome.title()}")
