# Jogo dos Pinos
linhas = []
for i in range(7):
  linha = input()
  linhas.append(linha)

contadorJogadas = 0
for i, linha in enumerate(linhas):
  for j, char in enumerate(linhas[i]):
    if char == 'o':
      if linhas[i][j-1] == 'o' and linhas[i][j-2] == '-':
        contadorJogadas += 1
      if (linhas[i][j+1] == 'o' and linhas[i][j+2] == '-') and j < 5:
        contadorJogadas += 1
      if linhas[i-1][j] == 'o' and linhas[i-1][j] == '-':
        contadorJogadas += 1
      if (linhas[i+1][j] == 'o' and linhas[i+2][j] == '-') and i < 5:
        contadorJogadas += 1
print(contadorJogadas)

