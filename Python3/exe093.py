#Exercício Python #093 - Cadastro de Jogador de Futebol -> https://www.youtube.com/watch?v=5yKiud-YNaE&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=26

print(('=====')*20)
print('Bem vindo(a) - Cadastro de Jogador de Futebol')
print(('=====')*20)

jogador = {}
somaGols = 0
jogador['nomeJogador'] = input('Nome do jogador: ')
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nomeJogador"]} jogou? '))
golsPartidas = []
for p,i in enumerate(range(0,jogador["partidas"])):
    gols = int(input(f'Quantos gols {jogador["nomeJogador"]} fez na {p+1} partida? '))
    golsPartidas.append(gols)
    somaGols += gols
jogador['gols'] = golsPartidas
jogador['total'] = somaGols
print(('=====')*20)
print(jogador)
print(('=====')*20)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
print(('=====')*20)
print(f'O jogador {jogador["nomeJogador"]} jogou {jogador["partidas"]} partidas')
for p, e in enumerate(golsPartidas):
    print(f'==> na partida {p+1}, fez {e} gols. ')
print(f'Foi um total de {somaGols} gols.')
print()