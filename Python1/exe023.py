# Exercicio 23 - Analisador de Números -> https://www.youtube.com/watch?v=wD2aerLMBWA&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=24&pp=iAQB

print(('==*==')*20)
print('Bem vindo(a) - Analisador de Números')
print(('==*==')*20)

número = int(input("Informe um número entre 1 e 9999: "))
print(f"Analisando o número {número}..")
if número < 10000:
  u = número // 1 % 10
  d = número // 10 % 10
  c = número // 100 % 10
  m = número // 1000 % 10
  print(f"Unidade: {u}")
  print(f"Dezena: {d}")
  print(f"Centena: {c}")
  print(f"Milhar: {m}")
elif número >= 10000:
      print('Você digitou um número inválido!')