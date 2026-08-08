# Dona Formiga

primeiraLinha = [int(x) for x in input().split(' ')]

quantidadeSaloes = primeiraLinha[0] # S
quantidadeTuneis = primeiraLinha[1] # T
salaoInicial     = primeiraLinha[2] # P

alturasSaloes = [int(x) for x in input().split(' ')].sort(reverse=True)
saloesPorAltura = {sorted(alturasSaloes, reverse=True)[x]: x+1 for x in range(len(alturasSaloes))}

tuneis = []

for i in range(quantidadeTuneis):
    tuneis.append([int(x) for x in input().split(' ')])

print(saloesPorAltura)
