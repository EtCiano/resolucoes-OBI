# # metrô da Nlogônia (metra.py)
# quantidade = [int(x) for x in input().split(' ')]

# estacoesC = {}
# for i in range(quantidade[0]-1):
#   estacao = [int(x) for x in input().split(' ')]
#   estacoesC.setdefault(estacao[0], []).append(estacao[1])
#   estacoesC.setdefault(estacao[1], []).append(estacao[0])

# estacoesQ = {}
# for i in range(quantidade[1]-1):
#   estacao = [int(x) for x in input().split(' ')]
#   estacoesQ.setdefault(estacao[0], []).append(estacao[1])
#   estacoesQ.setdefault(estacao[1], []).append(estacao[0])

# print("Estações C:")
# for key, value in estacoesC.items():
#     print(f"  {key}: {value}")
# print("\nEstações Q:")
# for key, value in estacoesQ.items():
#     print(f"  {key}: {value}")
