from math import gcd
from functools import reduce
from itertools import combinations_with_replacement

def checarCandidato(listaNumeros):

    candidato = False

    if len(listaNumeros) > 1:
        candidato = reduce(gcd, listaNumeros) > 1
    elif len(listaNumeros) == 1:
        candidato = gcd(listaNumeros[0]) > 1

    return candidato

def checarSubconjuntos(listaProteinas):

    contagem = 0

    for indices in combinations_with_replacement(range(1, len(listaProteinas)+1), 2):
        contagem += checarCandidato(listaProteinas[indices[0]-1:indices[1]])

    return contagem


primeiraLinha = [int(x) for x in input().split()]

quantSequencias = primeiraLinha[0]
quantOperacoes = primeiraLinha[1]

cadeia = [int(x) for x in input().split()]

for i in range(quantOperacoes):
    operacao = [int(x) for x in input().split()]
    if operacao[0] == 1:
        cadeia[operacao[1]-1] = operacao[2]
    if operacao[0] == 2:
        print(checarSubconjuntos(cadeia[operacao[1]-1:operacao[2]]))