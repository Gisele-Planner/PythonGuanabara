#Exercicio 04 - Discecando uma variável -> https://www.youtube.com/watch?v=tHYxjJxtJko&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=4&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a)!')
print(('==*==')*20)

a = input("Digite algo: ")
print("O tipo dessa variável é: ", type(a))
print("Só tem espaços? ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumérico?", a.isalnum())
print("Está em maiúsculas? ", a.isupper())
print("Está em minúsculas? ", a.islower())
print("Está capitalizada? ", a.istitle())
