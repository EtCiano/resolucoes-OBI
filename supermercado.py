# Supermercado (supermercado.py)
quantMercados = int(input())
precos = []
for i in range(quantMercados):
  proporcao = input().split(' ')
  proporcao[0] = float(proporcao[0])
  proporcao[1] = float(proporcao[1])
  taxa = 1000 / proporcao[1]
  proporcao[0] *= taxa
  precos.append(proporcao[0])

menor = precos[0]
for i, preco in enumerate(precos):
  if preco <= menor:
    menor = preco
print(f"{menor:.2f}")
