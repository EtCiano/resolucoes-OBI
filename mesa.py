# Mesa redonda (mesa.py)
cadeiras = [1, 2, 0]
numeros = [int(input()), int(input())]

loopCadeiras = [cadeiras*((numeros[0]//3)+1), cadeiras*((numeros[1]//3)+1)] # lista de cadeiras repetidas, baseado no número de Ana e Bea

cadeirasSelecionadas = [loopCadeiras[0][numeros[0]-1], loopCadeiras[1][numeros[1]-1]] # Cadeira que Ana e Bea cairíam (diminui por conta de arrays começarem em 0 enquanto o número começar em 1)

if cadeirasSelecionadas[0] == cadeirasSelecionadas[1]:
  cadeirasSelecionadas[1] = loopCadeiras[1][numeros[1]]

cadeiras.pop(cadeiras.index(cadeirasSelecionadas[0]))
cadeiras.pop(cadeiras.index(cadeirasSelecionadas[1]))
print(cadeiras[0])

