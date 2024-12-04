#Exercício Python #060 - Calculo de Fatorial-> https://www.youtube.com/watch?v=OBJL5vPj4-E&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=28

print(('\033[30m==*==')*20)
print('Bem vindo(a) ao Calculo de Fatorial')
print(('==*==')*20)

número = int(input('Digite um número para calcular o fatorial: '))
c = número
f = 1
while c > 0:
    print(f'{c}',' X ' if c> 1 else ' = ', end = '')
    f *= c
    c -=1    
print(f'{f} é o F! de {número}')