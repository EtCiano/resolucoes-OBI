# Camisetas da Olimpíada (camisetas.py)
quantidade = int(input())
camisasRequeridas = input().split(' ')
camisasRequeridas = [int(x) for x in camisasRequeridas]
camisasP = int(input())
camisasM = int(input())
if camisasP == camisasRequeridas.count(1) and camisasM == camisasRequeridas.count(2):
  print('S')
else:
  print('N')
