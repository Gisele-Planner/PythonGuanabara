'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
 Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
def aumentar(valor,fator=0, format=False):
    calculo = valor * (1+(fator/100))
    novoValor = round(calculo,2)
    return novoValor if format is False else moeda(novoValor)

def diminuir(valor,fator=0, format=False):
    calculo = valor * (1-(fator/100))
    novoValor = round(calculo,2)
    return novoValor if format is False else moeda(novoValor)

def dobro(valor, format=False):
    calculo = valor * 2
    novoValor = round(calculo,2)
    return novoValor if format is False else moeda(novoValor)

def metade(valor, format=False):
    calculo = valor / 2
    novoValor = round(calculo,2)
    return novoValor if format is False else moeda(novoValor)

def moeda(valor=0,pais='R$'):
    return f'{pais}{valor:.2f}'.replace('.',',')

def resumo(valor,aumenta,diminui):
    print('-'*40)
    print('Resumo do Valor'.center(40))
    print('-'*40)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do Preço: \t{dobro(valor,True)}')
    print(f'Metade do Preço: \t{metade(valor,True)}')
    print(f'{aumenta}% de Aumento: \t{aumentar(valor,aumenta,True)}')
    print(f'{diminui}% de Redução: \t{diminuir(valor,diminui,True)}')
    print('-'*40)

def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;30;41mErro: \"{entrada}\" é um número inválido\033[m')
        else:
            válido = True
            return float(entrada)
        
# print(moeda(20,'USS ')) #Exemplo Implementação Moeda
# resumo(200,10,20) #Exemplo Implementação Resumo
