pontuacoes = []

for i in range(5):
    pontuacoes.append(int(input()))

quantidades = [pontuacoes.count(x) for x in sorted(list(set(pontuacoes)))[::-1]]

if len(quantidades) == 1: quantidades.append(0)

print(quantidades[0], quantidades[1])