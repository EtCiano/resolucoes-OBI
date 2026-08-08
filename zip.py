# zip
lia1 = int(input())
lia2 = int(input())
carol1 = int(input())
carol2 = int(input())
cartas = [[lia1, lia2], [carol1, carol2]]
pontuacao = [0, 0]
for i in range(2):
  if cartas[i][0] == cartas[i][1]:
    modificador = 2
  elif (cartas[i][0] == cartas[i][1] - 1) or (cartas[i][1] == cartas[i][0] - 1):
    modificador = 3
  else:
    modificador = 1
  pontuacao[i] = (cartas[i][0] + cartas[i][1])*modificador
if pontuacao[1] < pontuacao[0]:
  print("Lia")
elif pontuacao[0] < pontuacao[1]:
  print("Carolina")
else:
  print("empate")
