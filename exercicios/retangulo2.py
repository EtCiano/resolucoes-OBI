# feito com IA, para aprendizado

import numpy as np

def resolver(n, arcos):
    posicoes = np.concatenate(([0], np.cumsum(arcos)[:-1]))
    total = sum(arcos)

    # Se o total for ímpar, metade não é inteira -> impossível ter oposto exato
    if total % 2 != 0:
        return "N"

    metade = total // 2
    opostos = (posicoes + metade) % total

    # broadcasting: compara cada posição real com cada oposto calculado
    matriz_bate = posicoes[:, None] == opostos[None, :]

    pares = matriz_bate.sum() // 2
    return "S" if pares >= 2 else "N"


n = int(input())
arcos = list(map(int, input().split()))
print(resolver(n, arcos))