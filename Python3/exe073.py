#exercicio 073 - Exercício Python #073 - Tuplas com Times de Futebol -> https://www.youtube.com/watch?v=RexybLcGewA&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=3

print(('==*==')*20)
print('Bem vindo(a) - Exercício Python #073 - Tuplas com Times de Futebol')
print(('==*==')*20)

#tabela retirada de https://ge.globo.com/futebol/brasileirao-serie-a/ em 18/09/2024
times = ("Botafogo","Palmeiras","Fortaleza","Flamengo","São Paulo","Bahia","Cruzeiro","Internacional","Vasco"
                             ,"Atlético-MG","Juventude","Bragantino","Athletico-PR","Grêmio","Criciúma","Fluminense","Vitória"
                             ,"Corinthians","Cuiabá","Atlético-GO")

print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(('====')*20)
print(f'Os 4 últimos colocados são: {times[16:]}')
print(('====')*20)
print(f'Os times em ordem alfábetica são: {sorted(times)}')
print(('====')*20)
print(f'O Palmeiras estão na posição: {(times.index('Palmeiras'))+1}ª Posição no campeonato Brasileiro')
print(('====')*20)
