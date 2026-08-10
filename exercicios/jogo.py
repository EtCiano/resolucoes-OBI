# # Jogo do Preto e Branco (jogo.py)
# tamanhoTabuleiro = [int(x) for x in input().split(' ')]
# tabuleiro = []
# for i in range(tamanhoTabuleiro[0]):
#   tabuleiro.append([])
#   for j in range(tamanhoTabuleiro[1]):
#     tabuleiro[i].append('b')
# quantidadePretas = int(input())

# pretas = []
# brancas = []
# for r in range(tamanhoTabuleiro[0]):
#   for c in range(tamanhoTabuleiro[1]):
#     if tabuleiro[r][c] == 'b':
#       brancas.append([r, c])
# for i in range(quantidadePretas):
#   peca = [int(x)-1 for x in input().split(' ')]
#   pretas.append(peca)
#   tabuleiro[peca[0]][peca[1]] = 'p'

# for i, preta in enumerate(pretas):
#   pecaX = preta[0]
#   pecaY = preta[1]
#   for direction_case in range(4):
#     match direction_case:
#       case 0:
#         x = pecaX-1
#         y = pecaY
#       case 1:
#         x = pecaX
#         y = pecaY-1
#       case 2:
#         x = pecaX
#         y = pecaY+1
#       case 3:
#         x = pecaX+1
#         y = pecaY
#     if 0 <= x < len(tabuleiro):
#       if 0 <= y < len(tabuleiro[x]):
#         if tabuleiro[x][y] == '-':
#           tabuleiro[x][y] = 'b'
#           brancas.append([x, y])

# for i, branca in enumerate(brancas):
#   pecaX = branca[0]
#   pecaY = branca[1]
#   pecasVizinhas = []
#   for direction_case in range(4):
#     match direction_case:
#       case 0:
#         x = pecaX-1
#         y = pecaY
#       case 1:
#         x = pecaX
#         y = pecaY-1
#       case 2:
#         x = pecaX
#         y = pecaY+1
#       case 3:
#         x = pecaX+1
#         y = pecaY

#     if 0 <= x < len(tabuleiro):
#       if 0 <= y < len(tabuleiro[x]):
#         if tabuleiro[x][y] == 'b':
#           pecasVizinhas.append([x, y])
#   if len(pecasVizinhas) == 1:
#     brancas.remove([pecasVizinhas[0][0], pecasVizinhas[0][1]])
#     tabuleiro[pecasVizinhas[0][0]][pecasVizinhas[0][1]] = '-'
#   elif len(pecasVizinhas) > 1:
#     brancas.remove(branca)
#     tabuleiro[pecaX][pecaY] = '-'

# print(len(brancas))
# for linha in tabuleiro:
#   print(" ".join(linha)) # o exercício não expecifíca a ordem para checar as peças brancas, e isso acaba sendo vital por que se eu colocar checar uma peça branca errada, todo as outras podem ser afetadas
