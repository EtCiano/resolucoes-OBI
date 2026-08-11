# Sanduíche (sanduiche.py)
primeiraLinha = [int(x) for x in input().split()]
quantidadeIngredientes = primeiraLinha[0]
quantidadeIncompativeis = primeiraLinha[1]

incompativeis = []

for i in range(quantidadeIncompativeis):
  incompativeis.append(input().replace(" ", ""))

combinacoes = []

for i in range(quantidadeIngredientes+1):
  for j in range(quantidadeIngredientes+1):
    combinacao = str(i) + str(j)
    # não funciona com combinações de 3 ingredientes ou mais
    # não sei se tem combinação de mais de 3 ingredientes
    if i == j:
      continue
    if combinacao in incompativeis or combinacao[::-1] in incompativeis:
      continue
    if combinacao in combinacoes or combinacao[::-1] in combinacoes:
      continue

    combinacoes.append(combinacao)

print(len(combinacoes))