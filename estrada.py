# Estrada (estrada.py)
compEstrada = int(input())
quantCidades = int(input())

distanciasCidades = []
for i in range(quantCidades):
  distanciasCidades.append(int(input()))

menorDistancia = 0.00
menorDistancia += float(compEstrada)
for i, distancia in enumerate(distanciasCidades):
  if distancia == distanciasCidades[-1]:
    vizinhanca = abs(((distanciasCidades[-2] + distanciasCidades[-1])/2)-compEstrada)
  else:
    vizinhanca = (distancia + distanciasCidades[i+1])/2
  if vizinhanca < menorDistancia:
    menorDistancia = 0.00
    menorDistancia += vizinhanca
print(f"{menorDistancia:.2f}")

