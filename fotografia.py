# Fotografia
fotografia = [int(x) for x in input().split(' ')]
quantidadeMolduras = int(input())
molduras = []
for i in range(quantidadeMolduras):
  molduras.append([int(x) for x in input().split(' ')])

diferencas = []
areaFotografia = fotografia[0] * fotografia[1]
for i, moldura in enumerate(molduras):
  areaMoldura = moldura[0] * moldura[1]
  diferenca = areaMoldura - areaFotografia
  if diferenca < 0:
    diferencas.append(1234567890)
  else:
    diferencas.append(areaMoldura - areaFotografia)

if min(diferencas) == 1234567890:
  print(-1)
else:
  print(diferencas.index(min(diferencas))+1)
