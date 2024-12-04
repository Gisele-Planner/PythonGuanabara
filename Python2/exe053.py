#Exercício Python #053 -  Palindromo -> https://www.youtube.com/watch?v=Er5Hyd4LyVw&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=20


print(('\033[30m==*==')*20)
print('Bem vindo(a) ao Validador de Palindromo')
print(('==*==')*20)

frase = input("Digite uma frase: ").strip().lower()
fraseSeparada = frase.split()
juntar = ''.join(fraseSeparada)
inverso = juntar[::-1]
if frase == inverso:
    print(f"{frase} é um palíndromo")
else:
    print(f"{frase} não é um palíndromo")
