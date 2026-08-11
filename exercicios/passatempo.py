tamanho = [int(x) for x in input().split()]

tabuleiro = []

variaveis = {}

for i in range(tamanho[0]+1):
    tabuleiro.append([x for x in input().split(' ')])

for i in range(tamanho[0]):
    for j in range(tamanho[1]):
        variaveis[tabuleiro[i][j]] = None

def calcularVariaveis(lista, sentido, pos):
    global variaveis

    numeroSoma = 0

    if sentido == 0: # Vertical
        numeroSoma = int(tabuleiro[tamanho[0]][pos])
    if sentido == 1: # Horizontal
        numeroSoma = int(tabuleiro[pos][tamanho[1]])

    semVariaveis = True

    for valor in variaveis.values():
        if valor is not None:
            semVariaveis = False


    if semVariaveis: # Não tem variaveis não nulas
        if len(set(lista)) == 1:
            variaveis[list(set(lista))[0]] = numeroSoma/tamanho[0 if sentido == 0 else 1]

    else:            # Tem variaveis não nulas
        variaveisNulas = [x for x in lista if variaveis[x] is None]

        variaveisNaoNulas = [x for x in lista if variaveis[x] is not None]

        somaNaoNulas = 0

        for variavelNaoNula in variaveisNaoNulas:
            somaNaoNulas += variaveis[variavelNaoNula]

        if len(set(variaveisNulas)) == 1:
            variaveis[variaveisNulas[0]] = (numeroSoma-somaNaoNulas)/len(variaveisNulas)

def checarTabuleiro(sentido, pos):
    global variaveis
    global tela

    if sentido == 0: # Vertical

        coluna = []

        for y in range(tamanho[0]):
            coluna.append(tabuleiro[y][pos])

        calcularVariaveis(coluna, sentido, pos)

    if sentido == 1: # Horizontal

        linha = []

        for x in range(tamanho[1]):
            linha.append(tabuleiro[pos][x])

        calcularVariaveis(linha, sentido, pos)

def checarNulo():
    global tabuleiro

    for valor in variaveis.values():
        if valor is None:
            return True

    return False

while checarNulo():
    for i in range(tamanho[1]):
        checarTabuleiro(0, i)
    for i in range(tamanho[0]):
        checarTabuleiro(1, i)

variaveisOrdenadas = dict(sorted(variaveis.items()))

for chave, valor in variaveisOrdenadas.items():
    print(chave, int(valor))
