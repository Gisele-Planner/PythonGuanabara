cores = ('\033[m',          #0 - Sem Cores
         '\033[0;30;41m',   #1 - Vermelho
         '\033[0;30;42m',   #2 - Verde
         '\033[0;30;43m',   #3 - Amarelo
         '\033[0;30;44m',   #4 - Azul
         '\033[0;30;45m',   #5 - Roxo
         '\033[7;30m',      #6 - Branco
         )

def título(msg, cor = 0):
    tam = len(msg)+3                #Definição do tamanho do titúlo
    print(cores[cor],end='')        #Inicio da Cor escolhida
    print('~' * tam)                #Sequencia de ~ antes titulo
    print(f'   {msg}')              #Título Formatado
    print('~' * tam)                #Sequencia de ~ após titulo
    print(cores[0],end='')          #Fim da Cor escolhida

#Implementação de Exemplo
# título('Exercício Python #107 - Exercitando módulos em Python',3)

def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;30;41mErro: \"{entrada}\" é um número inválido\033[m')
        else:
            válido = True
            return float(entrada)