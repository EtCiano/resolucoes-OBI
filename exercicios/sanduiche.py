# Sanduíche (sanduiche.py)

primeiraLinha = [int(x) for x in input().split()]
quantidadeIngredientes = primeiraLinha[0]
quantidadeIncompativeis = primeiraLinha[1]

incompativeis = []

for i in range(quantidadeIncompativeis):
    incompativeis.append(input().split())

combinacoes = []

def checarBase(numero, base):
    numeroAbs = str(abs(int(numero)))
    numerosBase = "".join([str(x) for x in range(base+1)])
    return all(c in numerosBase for c in numeroAbs)

numeroMaximo = int('9' * quantidadeIngredientes)

for i in range(numeroMaximo + 1):
    if checarBase(i, quantidadeIngredientes) and '0' not in str(i):
        combinacoes.append(list(str(i)))

def combinacaoValida(combinacao):
    for digito in combinacao:
        if combinacao.count(digito) > 1:
            return False
    for incompativel in incompativeis:
        if set(incompativel).issubset(combinacao):
            return False
    return True

combinacoesVistas = set()
novaCombinacoes = []

for combinacao in combinacoes:
    if not combinacaoValida(combinacao):
        continue
    assinatura = tuple(sorted(combinacao))
    if assinatura in combinacoesVistas:
        continue
    combinacoesVistas.add(assinatura)
    novaCombinacoes.append(combinacao)

print(len(novaCombinacoes))