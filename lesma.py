# Dona Lesma (lesma.py)
altura = int(input())
distDia = int(input())
distNoite = int(input())

contadorDias = 0
distanciaMuro = 0

while True:
  contadorDias += 1
  distanciaMuro += distDia
  if distanciaMuro >= altura:
    break
  distanciaMuro -= distNoite

print(contadorDias)
