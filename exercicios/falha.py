quantSenhas = int(input())

senhas = []

for i in range(quantSenhas):
    senhas.append(input())

pares = []

for i, senha in enumerate(senhas):
    senhasCompativeis = [[senha, x] for j, x in enumerate(senhas) if x in senha and i != j]
    pares.extend(senhasCompativeis)

print(len(pares))