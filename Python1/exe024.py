# Exercicio 024 - Analisador de Textos, precisa começar com 'santo' -> https://www.youtube.com/watch?v=QroT8cZMRnc&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=25&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Analisador de Textos - Inicio')
print(('==*==')*20)

cidade = input("Diga a cidade de nascimento: ").strip()
print('Analisando..')
cidade = cidade.lower()
print(cidade[:5] == 'santo')
#dessa forma ele pega os primeiros caracteres
