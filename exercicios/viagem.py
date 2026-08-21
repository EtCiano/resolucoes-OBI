# primeiraLinha = [int(x) for x in input().split()]
# valorTotal = primeiraLinha[0]
# quantIlhas = primeiraLinha[1]
# quantConexoes = primeiraLinha[2]

# conexoes = []

# for i in range(quantConexoes):
#     linha = [int(x) for x in input().split()]
#     conexoes.append({
#         'ilhaA': linha[0],
#         'ilhaB': linha[1],
#         'tempo': linha[2],
#         'preco': linha[3]
#     })

# ultimaLinha = [int(x) for x in input().split()]

# inicio = ultimaLinha[0]
# destino = ultimaLinha[1]

# rotas = []
# ilhasForam = []
# conexoesForam = []

# def calcularRotas(ilha):
#     global ilhasForam
#     global conexoes
#     global quantIlhas

#     if ilha == destino:
#         return

#     conexoesPossiveis = [x for x in conexoes if ilha in list(x.values())[:2]]

#     rota = []

#     for conexao in conexoesPossiveis:
#         rota.append(conexao)
#         for ilhaConectada in list(conexao.values())[:2]:
#             if ilhaConectada == ilha or ilhaConectada in ilhasForam:
#                 continue

#             ilhasForam.append(ilha)
            
#             print(ilhaConectada)

#             rota.append(calcularRotas(ilhaConectada))

#     return rota

# print(calcularRotas(inicio))