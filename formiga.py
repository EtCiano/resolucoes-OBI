# Dona Formiga

primeiraLinha = [int(x) for x in input().split(' ')]

quantidadeSaloes   = primeiraLinha[0] # S
quantidadeTuneis   = primeiraLinha[1] # T
salaoInicialIndice = primeiraLinha[2] # P

alturaPorSalao = [int(x) for x in input().split(' ')]

tuneis = []

saloesPorAltura = {
    alturaPorSalao[x]: {
        'posicao': x + 1,
        'altura': alturaPorSalao[x],
        'conexoes': [],
        'conexoesViaveis': [],
    }
    for x in range(len(alturaPorSalao))
}

for i in range(quantidadeTuneis):
    conexao = [int(x) for x in input().split(' ')]
    tuneis.append(conexao)

    saloesPorAltura[alturaPorSalao[conexao[0]-1]]['conexoes'].append(conexao[1])
    saloesPorAltura[alturaPorSalao[conexao[1]-1]]['conexoes'].append(conexao[0])


memo = {}

def calcularMaiorCaminho(indice_salao):
  if indice_salao in memo:
    return memo[indice_salao]

  altura = alturaPorSalao[indice_salao - 1]
  salao = saloesPorAltura[altura]

  maior_subcaminho = 0

  for vizinho in salao['conexoesViaveis']:
    maior_subcaminho = max(maior_subcaminho, calcularMaiorCaminho(vizinho))

  memo[indice_salao] = 1 + maior_subcaminho
  return memo[indice_salao]


for i, altura in enumerate(alturaPorSalao):
  salao = saloesPorAltura[altura]
  for j, conexao in enumerate(salao['conexoes']):
    viavel = alturaPorSalao[conexao - 1] < salao['altura']
    if viavel:
      salao['conexoesViaveis'].append(conexao)
else:
  # salaoInicial = saloesPorAltura[alturaPorSalao[salaoInicialIndice]]
  caminhos = calcularMaiorCaminho(salaoInicialIndice)
  print(caminhos-1)