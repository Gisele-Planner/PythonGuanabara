#Exercício Python #071 - Simulador de Caixa Eletrônico -> https://www.youtube.com/watch?v=_XGgwltYpYk&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=41

print(('==*==')*20)
print('Bem vindo(a) - Simulador de Caixa Eletrônico')
print(('==*==')*20)
print('Banco do Silva')
print(('====')*20)

listaCedulas = [50,20,10,1]
valor = int(input('Qual valor deseja sacar? R$ '))
contador = 0
saldo = valor

while contador < len(listaCedulas) and saldo != 0:
    cedula = listaCedulas[contador]
    divInteiro = int(saldo/cedula)
    if valor == 0:
        break
    elif saldo % cedula == 0 and saldo == 0:
        print(f'Total de {divInteiro} cédulas de R$ {cedula}')
        saldo = saldo - (cedula * divInteiro)        
    else:
        if divInteiro == 0:
            contador += 1
        else:
            print(f'Total de {divInteiro} cédulas de R$ {cedula}')
            saldo = saldo - (cedula * divInteiro)
            contador += 1

print(('====')*20)
print('Volte sempre ao Banco do Silva')  
    


